from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Email
from .tasks import send_email


class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'origin', 'destination', 'status')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})},
    }

    def save_model(self, request, obj, form, change):
        super(EmailAdmin, self).save_model(request, obj, form, change)
        send_email.delay(email_id=obj.id)

admin.site.register(Email, EmailAdmin)
