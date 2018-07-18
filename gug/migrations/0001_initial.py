# Generated by Django 2.0.7 on 2018-07-17 17:02

from django.db import migrations, models
import django.db.models.deletion
import gug.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(help_text='Unique reference ID for this domain', max_length=100, unique=True)),
                ('name', models.CharField(blank=True, help_text='Short descriptive name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Google_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('scope', models.CharField(max_length=200)),
                ('discovery', models.CharField(max_length=200)),
                ('secret_json', models.TextField(blank=True, default='{}', null=True, validators=[gug.models.validate_json])),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(help_text='Unique reference ID for this metric within the domain', max_length=100)),
                ('name', models.CharField(blank=True, help_text='Short descriptive name', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gug.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='metric',
            unique_together={('domain', 'ref')},
        ),
    ]