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


class CheckEmailPhoneNumberAPIView(APIView):

    def post(self, request):
        try:
            email = request.data['email']
            phone_number = request.data['phone_number']
            if email == "" or phone_number == "":
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Email and phone number '
                                                                                     'should not be empty'})

            try:
                messages = {}
                client = Client.objects.get(email=email)
                if client.email == email:
                    messages['msg_email'] = f'User with email {client} already exists as a client'
                if client.phone_number == phone_number:
                    messages['msg_phone'] = f'User with phone number {client.phone_number} already exists as a client'

                return Response(status=status.HTTP_200_OK, data={'response': messages,
                                                                 'status': 'Successful',
                                                                 'HTTP status code': 200
                                                                 })

            except:
                try:
                    messages = {}
                    delivery_person = DeliveryPerson.objects.get(email=email)
                    if delivery_person.email == email:
                        messages['msg_email'] = f'User with email {delivery_person} already exists as a client'
                    if delivery_person.phone_number == phone_number:
                        messages['msg_phone'] = f'User with phone number {delivery_person.phone_number} already exists as a client'

                    return Response(status=status.HTTP_200_OK, data={'response': messages,
                                                                     'status': 'Successful',
                                                                     'HTTP status code': 200
                                                                     })
                except:
                    try:
                        messages = {}
                        admin_user = AdminUser.objects.get(email=email)
                        if admin_user.email == email:
                            messages['msg_email'] = f'User with email {admin_user} already exists'
                        if admin_user.phone_number == phone_number:
                            messages['msg_phone'] = f'User with phone number {admin_user.phone_number} already exists'

                        return Response(status=status.HTTP_200_OK, data={'response': messages,
                                                                         'status': 'Successful',
                                                                         'HTTP status code': 200
                                                                         })

                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST, data={'response': 'User does not exist',
                                                                                  'status': 'Unsuccessful',
                                                                                  'HTTP status code': 400
                                                                                  })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Something went wrong!'})
