# Generated by Django 2.0.7 on 2018-07-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0022_google_service_service_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='google_service',
            name='service',
        ),
    ]
