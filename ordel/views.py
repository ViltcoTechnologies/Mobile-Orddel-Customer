from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django_email_verification import sendConfirm
from ordel.verificaton import TwilioVerification
from client_app.models import Client
from delivery_app.models import DeliveryPerson
from admin_dashboard.models import AdminUser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


class ResendOtpApiView(APIView):

    def post(self, request):
        try:
            phone_number = request.data['phone_number']
            try:
                twilio_verification = TwilioVerification(str(phone_number))
                twilio_verification.update_status()
                twilio_verification.send_otp()
                return Response(status=status.HTTP_200_OK,
                                data="Verification code resent")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="There was a error sending "
                                     "Verification code")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! phone_number is required")


class VerifyPhoneNumberApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        try:
            phone_number = request.data['phone_number']
            verification_code = request.data['verification_code']
            user_type = request.data['user_type'].lower()
            print(verification_code)
            try:
                twilio_verification = TwilioVerification(
                    str(phone_number),
                    str(verification_code)
                )
                verification = twilio_verification.verify_otp()
                if verification == "approved":
                    if user_type == "client":
                        saved_user = Client.objects.filter(phone_number=phone_number)
                    if user_type == "delivery_person":
                        saved_user = DeliveryPerson.objects.filter(phone_number=phone_number)
                    saved_user.update(
                        otp_status=True
                    )
                    return Response(status=status.HTTP_200_OK,
                                    data={"message": "Verification successful"})
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The verification was not "
                                                 "successful"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "Twilio server is down, "
                                                 "please try again later"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "you're missing one of the following "
                                             "required field (phone_number, "
                                             "verification_code or user_type"})


class VerifyPhoneNumberV2ApiView(APIView):

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        try:
            phone_number = request.data['phone_number']
            verification_code = request.data['verification_code']
            # user_type = request.data['user_type'].lower()
            print(verification_code)
            try:
                twilio_verification = TwilioVerification(
                    str(phone_number),
                    str(verification_code)
                )
                verification = twilio_verification.verify_otp()
                if verification == "approved":
                    # if user_type == "client":
                    #     saved_user = Client.objects.filter(phone_number=phone_number)
                    # if user_type == "delivery_person":
                    #     saved_user = DeliveryPerson.objects.filter(phone_number=phone_number)
                    # saved_user.update(
                    #     otp_status=True
                    # )
                    return Response(status=status.HTTP_200_OK,
                                    data={"message": "Verification successful"})
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The verification code is invalid"})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={"message": "The verification code is invalid"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "you're missing one of the following "
                                             "required field (phone_number, "
                                             "verification_code or user_type"})


class SendOTPAPIView(APIView):

    def post(self, request):
        try:
            phone_number = request.data['phone_number']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Phone number not entered'})
        try:
            twilio_verification = TwilioVerification(str(phone_number))
            twilio_verification.send_otp()
            return Response(status=status.HTTP_200_OK, data={'message': 'OTP sent'})

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to send OTP'})


# class CheckEmailPhoneNumberAPIView(APIView):
#
#     def post(self, request):
#         try:
#             email = request.data['email']
#             phone_number = request.data['phone_number']
#             if email == "" or phone_number == "":
#                 return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Email and phone number '
#                                                                                      'should not be empty'})
#
#             try:
#                 messages = {}
#                 client = Client.objects.get(email=email)
#                 if client.email == email:
#                     messages['msg_email'] = f'User with email {client} already exists as a client'
#                 if client.phone_number == phone_number:
#                     messages['msg_phone'] = f'User with phone number {client.phone_number} already exists as a client'
#
#                 return Response(status=status.HTTP_200_OK, data={'response': messages,
#                                                                  'status': 'Successful',
#                                                                  'HTTP status code': 200
#                                                                  })
#
#             except:
#                 try:
#                     messages = {}
#                     delivery_person = DeliveryPerson.objects.get(email=email)
#                     if delivery_person.email == email:
#                         messages['msg_email'] = f'User with email {delivery_person} already exists as a delivery person'
#                     if delivery_person.phone_number == phone_number:
#                         messages['msg_phone'] = f'User with phone number {delivery_person.phone_number} already exists as a delivery person'
#
#                     return Response(status=status.HTTP_200_OK, data={'response': messages,
#                                                                      'status': 'Successful',
#                                                                      'HTTP status code': 200
#                                                                      })
#                 except:
#                     try:
#                         messages = {}
#                         admin_user = AdminUser.objects.get(email=email)
#                         if admin_user.email == email:
#                             messages['msg_email'] = f'User with email {admin_user} already exists'
#                         if admin_user.phone_number == phone_number:
#                             messages['msg_phone'] = f'User with phone number {admin_user.phone_number} already exists'
#
#                         return Response(status=status.HTTP_200_OK, data={'response': messages,
#                                                                          'status': 'Successful',
#                                                                          'HTTP status code': 200
#                                                                          })
#
#                     except:
#                         return Response(status=status.HTTP_400_BAD_REQUEST, data={'response': 'User does not exist',
#                                                                                   'status': 'Unsuccessful',
#                                                                                   'HTTP status code': 400
#                                                                                   })
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Something went wrong!'})

class CheckEmailAPIView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            if email == "":
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Email field is '
                                                                                     'required'})
            try:
                client = Client.objects.get(username=email)
                return Response(status=status.HTTP_200_OK, data={'message': f'This email '
                                                                            f'already exists as '
                                                                            f'a client'})
            except:
                try:
                    delivery_person = DeliveryPerson.objects.get(username=email)
                    return Response(status=status.HTTP_200_OK, data={'message': f'This email '
                                                                                f'already exists as a '
                                                                                f'delivery person'})
                except:
                    try:
                        admin_user = AdminUser.objects.get(username=email)
                        return Response(status=status.HTTP_200_OK, data={'message': f'This email '
                                                                                    f'already exists'})
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User does not exist'})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Something went wrong'})


class CheckPhoneAPIView(APIView):
    def post(self, request):
        try:
            phone = request.data['phone']
            if phone == "":
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Email field is '
                                                                                     'required'})
            try:
                client = Client.objects.get(phone_number=phone)
                return Response(status=status.HTTP_200_OK, data={'message': f'This phone number '
                                                                            f'already exists as '
                                                                            f'a client'})
            except:
                try:
                    delivery_person = DeliveryPerson.objects.get(phone_number=phone)
                    return Response(status=status.HTTP_200_OK, data={'message': f'This phone number '
                                                                                f'already exists as a '
                                                                                f'delivery person'})
                except:
                    try:
                        admin_user = AdminUser.objects.get(phone_number=phone)
                        return Response(status=status.HTTP_200_OK, data={'message': f'This phone number '
                                                                                    f'already exists'})
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': f'User does not exist'})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Something went wrong'})


# Password Reset Funtionality
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_token.key
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="ORDDEL"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetEmailAndPhoneApiView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            user_type = request.data['user_type']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'username and/or user_type not provided'})
        if user_type == 'client':
            try:
                client = Client.objects.get(username=username)
                data = {'email': client.email, 'phone': client.phone_number}
                return Response(status=status.HTTP_200_OK, data={'data': data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'user not found'})
        elif user_type == 'delivery_person':
            try:
                delivery_person = DeliveryPerson.objects.get(username=username)
                data = {'email': delivery_person.email, 'phone': delivery_person.phone_number}
                return Response(status=status.HTTP_200_OK, data={'data': data})
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'user not found'})


class ChangePasswordViaPhoneNumber(APIView):
    def post(self, request):
        username = request.data['username']
        new_password = request.data['password']
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK, data = {'message': 'Password Updated successfully'})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User not found'})

