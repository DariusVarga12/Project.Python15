from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.urls import reverse
from .forms import AppointmentForm, AppointmentDetailsForm
from .models import Service, Appointment
import logging

logger = logging.getLogger(__name__)


def get_all_services(request):
    services = Service.objects.all()
    return render(request, "services_list.html", {
        "services": services
    })

def create_appointment(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404(f"Service with ID = {service_id} does not exist.")

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.service = service
            appointment.save()

            if Appointment.objects.filter(pk=appointment.id).exists():
                logger.info("Appointment saved successfully.")
            else:
                logger.warning("Failed to save appointment.")

            appointment_id = appointment.id

            return redirect(reverse('appointment_details', kwargs={'appointment_id': appointment_id}))
    else:
        form = AppointmentForm()

    return render(request, 'booking.html', {'service': service, 'form': form})


def delete_appointment(request, appointment_id):
    Appointment.objects.filter(id=appointment_id).delete()
    services = Service.objects.all()
    return render(request, "services_list.html", {
        "services": services
    })


def get_service(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404(f"Service with ID = {service_id} does not exist.")

    hours = []
    start_hour = 10
    end_hour = 20
    for hour in range(start_hour, end_hour + 1):
        hour_str = f"{hour:02}:00"
        hours.append(hour_str)

    return render(request, "booking.html",
        {
            "service": service,
            "hours": hours,
            "form": AppointmentForm()
        })


def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    form = AppointmentDetailsForm(instance=appointment)
    service = appointment.service

    all_appointemnts = return_all_appointments(appointment.first_name)

    return render(request, 'appointment_details.html', {'form': form, 'service': service, 'all_appointments': all_appointemnts})


def return_all_appointments(user_name):
    appointments = Appointment.objects.all().filter(first_name=str(user_name).capitalize())

    if appointments.exists():
        print("Există program.")
    else:
        print("Nu există program.")

    return appointments
