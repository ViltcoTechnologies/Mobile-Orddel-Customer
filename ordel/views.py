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
                                    data="Verification successful")
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
