from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = 'ACb91fa80f036c5ee2e25b60ced5b70871'
        self.auth_token = '9065fc9f95a37116d5f07b8a05e2f933'
        self.virtual_number = '+12543234708'
        self.verified_number = '+380995327348'

        self.client = Client(self.account_sid, self.auth_token)


    def send_sms(self, message):
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': 'https_proxy'}

        message = self.client.messages.create(
            body=message,
            from_=self.virtual_number,
            to=self.verified_number
        )

        print(message.sid)