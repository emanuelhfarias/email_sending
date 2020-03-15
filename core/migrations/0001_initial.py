# Generated by Django 3.0.4 on 2020-03-15 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=256)),
                ('origin', models.EmailField(max_length=254, verbose_name='From')),
                ('destination', models.TextField(help_text='Comma separated emails: x@test.com, y@test.com', verbose_name='To')),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Sent', 'Sent')], default='Pending', editable=False, max_length=15)),
            ],
        ),
    ]
