# Generated by Django 2.0.7 on 2018-07-24 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0025_auto_20180719_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['start_date']},
        ),
    ]