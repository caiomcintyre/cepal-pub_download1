# Generated by Django 2.0.7 on 2019-01-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0041_auto_20190102_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workarea',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
