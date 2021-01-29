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

    def post(self, request):
        try:
            phone_number = request.data['phone_number']
            verification_code = request.data['verification_code']
            user_type = request.data['user_type'].lower()
            if user_type == "client":
                try:
                    twilio_verification = TwilioVerification(
                        str(phone_number),
                        str(verification_code)
                    )
                    twilio_verification.verify_otp()
                    client = Client.objects.get(phone_number=phone_number)
                    client.otp_status = True
                    return Response(status=status.HTTP_200_OK,
                                    data="Verification successful")
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="There was a error "
                                         "Verification code")
            elif user_type == "delivery_person":
                try:
                    twilio_verification = TwilioVerification(
                        str(phone_number),
                        str(verification_code)
                    )
                    twilio_verification.verify_otp()
                    delivery_person = DeliveryPerson.objects.get(phone_number=phone_number)
                    delivery_person.otp_status = True
                    return Response(status=status.HTTP_200_OK,
                                    data="Verification successful")
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="There was a error "
                                         "Verification code")
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Ooops! Invalid user_type "
                                     "choose between client, delivery_person")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! phone_number, verification_code "
                                 "and user_type is required")
