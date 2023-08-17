from email.header import Header
from email.utils import formataddr
from django.core.mail import send_mail
from django.conf import settings
from django.http import BadHeaderError
from rest_framework.response import Response
from rest_framework import status


class SendMail():
    from_email = formataddr((str(Header('Excel-Virtual', 'utf-8')), settings.EMAIL_HOST_USER))
    subject = 'Email verify account'
    message = 'This is my test send mail'
    
    def send_mail_verify(self, recipient_list, name, url):
        html_message = f"""
            <h2>Hi {name},</h2>
            <div>
                <h4>Please click link in below to verify your account!</h4></br>
                <a href="{url}">Link verify</a>
            </div>
        """

        try:
            send_mail(subject=self.subject, message=self.message, from_email=self.from_email, recipient_list=[recipient_list], fail_silently=False, html_message=html_message)
        except BadHeaderError as e:
            return Response({'data': e}, status=status.HTTP_400_BAD_REQUEST)
