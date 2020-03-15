from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'origin', 'destination', 'status')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})},
    }

admin.site.register(Email, EmailAdmin)
