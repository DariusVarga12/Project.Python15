from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.get_all_services, name='services_list'),
    path('services/<int:service_id>/', views.get_service, name='get_service'),
    path('services/<int:service_id>/booking/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:appointment_id>/', views.appointment_details, name='appointment_details'),
]
