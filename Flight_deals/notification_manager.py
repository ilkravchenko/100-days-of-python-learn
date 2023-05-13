from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import smtplib

MY_EMAIL = 'bilbob172839@gmail.com'
MY_PASSWORD = 'bswxpubchiudxhwi'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = 'ACb91fa80f036c5ee2e25b60ced5b70871'
        self.auth_token = '66186b42a7649c6993d2fa1d7281e10b'
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

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, 587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )