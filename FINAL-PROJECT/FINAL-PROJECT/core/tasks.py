# core/tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from .models import Employee

@shared_task
def notify_unregistered_employees():
    threshold_date = timezone.now() - timedelta(minutes=2)
    employees_to_notify = Employee.objects.filter(created_at__lt=threshold_date)
    
    for employee in employees_to_notify:

        subject = 'NOTIFICATION CONCERNED WITH REGISTRATION'
        message = f'Good Day, {employee.name}. NOTIFICATION CONCERNED WITH REGISTRATION'
        recipient_list = [employee.email]
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        print(f'Notification sent to: {employee.name} {employee.surname} ({employee.email})')