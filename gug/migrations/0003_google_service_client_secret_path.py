# Generated by Django 2.0.7 on 2018-07-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0002_auto_20180718_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='google_service',
            name='client_secret_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
