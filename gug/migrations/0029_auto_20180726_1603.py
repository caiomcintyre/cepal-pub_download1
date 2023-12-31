# Generated by Django 2.0.7 on 2018-07-26 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0028_auto_20180724_2035'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='metric',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='metric',
            name='domain',
        ),
        migrations.AlterModelOptions(
            name='google_service',
            options={'verbose_name': 'Google Service', 'verbose_name_plural': 'Google Services'},
        ),
        migrations.AlterModelOptions(
            name='service_type',
            options={'verbose_name': 'Service type', 'verbose_name_plural': 'Service types'},
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Metric',
        ),
    ]
