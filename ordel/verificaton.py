import random
import os
from twilio.rest import Client
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
service_sid = os.environ.get('SERVICE_SID')

client = Client(account_sid, auth_token)


class TwilioVerification:

    def __init__(self, phone_number, verification_code=""):
        self.phone_number = phone_number
        self.verification_code = verification_code

    def send_otp(self):
        verification = client.verify \
            .services(service_sid) \
            .verifications \
            .create(to=self.phone_number,
                    channel='sms',)

    def update_status(self):
        verification = client.verify \
            .services(service_sid) \
            .verifications(self.phone_number) \
            .update(status="canceled")

    def verify_otp(self):
        verification = client.verify \
                .services(service_sid) \
                .verification_checks \
                .create(to=self.phone_number, code=self.verification_code)
