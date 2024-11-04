# FINAL/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FINAL.settings')
app = Celery('FINAL')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# py -m celery -A FINAL worker -l info --pool=threads
# py -m celery -A FINAL beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler