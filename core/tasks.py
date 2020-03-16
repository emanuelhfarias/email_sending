from django.core.mail import send_mail
from celery import shared_task

from .models import Email

@shared_task
def send_email(email_id):
    email = Email.objects.get(id=email_id)
    try:
        send_mail(
            email.subject,
            email.message,
            email.origin,
            [e.strip() for e in email.destination.split(',')],
            fail_silently=True,
        )
        email.status = Email.SENT
    except Exception as e:
        email.status = Email.FAILED
    email.save()
