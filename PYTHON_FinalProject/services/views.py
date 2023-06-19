from django.shortcuts import render

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
    return render(request, "services.html", {
        "services": services
    })

def get_service(request):
    return render(request, "appointment_details.html")





