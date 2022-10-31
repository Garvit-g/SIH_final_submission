import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

SENDGRID_API_KEY='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'

message = Mail(
    from_email='mallasaianish@gmail.com',
    to_emails='mallasaianish@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)