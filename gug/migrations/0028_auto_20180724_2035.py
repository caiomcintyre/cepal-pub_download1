# Generated by Django 2.0.7 on 2018-07-24 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0027_auto_20180724_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dspace',
            old_name='mid',
            new_name='id_dspace',
        ),
    ]
