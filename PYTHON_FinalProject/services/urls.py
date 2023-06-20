from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_services, name='services_list'),
    path('<int:service_id>/', views.get_service, name='booking'),
    path('<int:service_id>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('<int:service_id>/details/', views.appointment_details, name='appointment_details'),
]