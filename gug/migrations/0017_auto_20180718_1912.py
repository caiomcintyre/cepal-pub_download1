# Generated by Django 2.0.7 on 2018-07-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0016_period_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='google_service',
            name='view_id',
            field=models.CharField(default='', max_length=30),
        ),
    ]