# Generated by Django 2.0.7 on 2018-07-19 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0023_remove_google_service_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='google_service',
            old_name='service_t',
            new_name='service',
        ),
    ]
