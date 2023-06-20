from django.utils import timezone
from .models import Appointment
from .views import send_reminder_notification

def send_reminder_for_upcoming_appointments():
    upcoming_appointments = Appointment.objects.filter(
        appointment_date__gte=timezone.now().date(),
        appointment_date__lte=timezone.now().date() + timezone.timedelta(days=7)
    )

    for appointment in upcoming_appointments:
        send_reminder_notification(
            email='user@example.com',  # Schimbă adresa de e-mail cu adresa utilizatorului curent
            service_name=appointment.service,
            appointment_date=appointment.appointment_date,
            appointment_time=appointment.appointment_time
        )