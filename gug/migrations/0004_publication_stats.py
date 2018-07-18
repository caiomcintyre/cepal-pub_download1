# Generated by Django 2.0.7 on 2018-07-18 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gug', '0003_google_service_client_secret_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turl', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuantity', models.BigIntegerField(null=True)),
                ('google_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gug.Google_service')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gug.Period')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gug.Publication')),
            ],
        ),
    ]