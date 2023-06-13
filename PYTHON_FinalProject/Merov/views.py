from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")

def services(request):
    return render(request, 'services/services.html')

def appointment_details(request):
    return render(request, 'services/appointment_details.html')
