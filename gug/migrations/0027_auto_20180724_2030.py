# Generated by Django 2.0.7 on 2018-07-24 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0026_auto_20180724_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dspace',
            old_name='id_dspace',
            new_name='mid',
        ),
    ]
