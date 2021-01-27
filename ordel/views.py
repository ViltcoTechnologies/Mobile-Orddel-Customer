from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django_email_verification import sendConfirm
from ordel.verificaton import TwilioVerification


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
            try:
                twilio_verification = TwilioVerification(
                    str(phone_number),
                    str(verification_code)
                )
                twilio_verification.verify_otp()
                return Response(status=status.HTTP_200_OK,
                                data="Verification code resent")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="There was a error sending "
                                     "Verification code")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data="Oops! phone_number is required")
