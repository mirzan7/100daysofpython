from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TWILIO_SID = 'secret'
TWILIO_AUTH_TOKEN = 'secret'
TWILIO_VIRTUAL_NUMBER = 'secret'
TWILIO_VERIFIED_NUMBER = 'secret'
MY_EMAIL= ''
My_PASSWORD = ""

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self,emails, message_text, google_link):

        message = MIMEMultipart()
        message["From"] = MY_EMAIL
        message["To"] = emails
        message["Subject"] = "Alert, cheap flight ticket found"

        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.starttls()
            server.login(MY_EMAIL, My_PASSWORD)
            server.sendmail(MY_EMAIL, emails, message.as_string())
        print("email send successfully")
