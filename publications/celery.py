from __future__ import absolute_import, unicode_literals
import os
from os import environ
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publications.settings')

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publications.settings')
app = Celery('pub_download', broker=environ.get('BROKER_URL'))
#app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
