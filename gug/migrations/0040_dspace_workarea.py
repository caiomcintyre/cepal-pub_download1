# Generated by Django 2.0.7 on 2019-01-02 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0039_workarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='dspace',
            name='workarea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gug.WorkArea'),
        ),
    ]
