from django.db import models


class Email(models.Model):
    PENDING = 'Pending'
    FAILED = 'Failed'
    SENT = 'Sent'
    STATUS_CHOICES = [
      (PENDING, PENDING.capitalize()),
      (FAILED, FAILED.capitalize()),
      (SENT, SENT.capitalize()),
    ]

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    subject = models.CharField(max_length=256, null=False, blank=False)
    origin = models.EmailField(verbose_name='From')
    destination = models.TextField(
      null=False, blank=False, verbose_name='To', help_text="Comma separated emails: x@test.com, y@test.com")
    message = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=PENDING, editable=False)
