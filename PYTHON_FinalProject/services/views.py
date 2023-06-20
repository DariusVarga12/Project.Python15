from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

services = [
    {
        "id": 1,
        "name": "(SkinFade/TaperFade)MEN",
        "price": 70.00
    },
    {
        "id": 2,
        "name": "(CUT&BEARD)MEN",
        "price": 80.00
    },
    {
        "id": 3,
        "name": "LADIES(full pack) short / medium hair / long hair",
        "price": 100.00
    },
]

def get_all_services(request):
    return render(request, "services_list.html", {
        "services": services
    })

def get_service(request, service_id):
    filtered_services = [
        service for service in services if service["id"] == service_id
    ]

    if len(filtered_services) == 0:
        raise Http404(f"Service with ID = {service_id} does not exist.")

    return render(request, "booking.html", {
        "service": filtered_services[0]
    })

def confirm_booking(request, service_id):
    filtered_services = [
        service for service in services if service["id"] == service_id
    ]

    if len(filtered_services) == 0:
        raise Http404(f"Service with ID = {service_id} does not exist.")

    if request.method == "POST":
        # Procesează datele trimise prin POST și salvează programarea în baza de date
        # Poți utiliza Django Forms pentru a valida și procesa datele

        # Redirecționează către pagina cu detaliile programării
        return HttpResponseRedirect(reverse("appointment_details", args=[service_id]))

    return render(request, "booking.html", {
        "service": filtered_services[0]
    })

def appointment_details(request, service_id):
    filtered_services = [
        service for service in services if service["id"] == service_id
    ]

    if len(filtered_services) == 0:
        raise Http404(f"Service with ID = {service_id} does not exist.")

    return render(request, "appointment_details.html", {
        "service": filtered_services[0]
    })
