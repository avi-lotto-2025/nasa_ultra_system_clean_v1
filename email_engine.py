import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailEngine:

    def __init__(self):
        self.sender = os.getenv("SENDER_EMAIL", "noreply@nasa-ultra.com")
        self.target = "avi5588@gmail.com"
        self.api_key = os.getenv("SENDGRID_API_KEY", "")

    def send(self, subject, body):
        if not self.api_key:
            return "NO_SENDGRID_KEY"

        msg = Mail(
            from_email=self.sender,
            to_emails=self.target,
            subject=subject,
            plain_text_content=body
        )

        try:
            sg = SendGridAPIClient(self.api_key)
            sg.send(msg)
            return "EMAIL_SENT"
        except Exception as e:
            return f"EMAIL_ERROR: {str(e)}"
