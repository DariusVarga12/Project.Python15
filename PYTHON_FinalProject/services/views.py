from django.shortcuts import render, Http404
from django.shortcuts import redirect
from .models import Service, Appointment

def get_all_services(request):
    services = Service.objects.all()
    return render(request, "services_list.html", {
        "services": services
    })

def get_service(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404(f"Service with ID = {service_id} does not exist.")
    return render(request, "booking.html", {
        "service": service
    })
def create_appointment(request, service_id):
    if request.method == 'POST':
        service = Service.objects.get(pk=service_id)
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        recurrence = request.POST['recurrence']
        email = request.POST['email']

        appointment = Appointment(service=service, appointment_date=appointment_date, appointment_time=appointment_time, recurrence=recurrence, email=email)
        appointment.save()
        return redirect('appointment_details', appointment_id=appointment.id)
    else:
        try:
            service = Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            raise Http404(f"Service with ID = {service_id} does not exist.")
        return render(request, 'booking.html', {'service': service})

def appointment_details(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        raise Http404(f"Appointment with ID = {appointment_id} does not exist.")
    return render(request, 'appointment_details.html', {'appointment': appointment})

