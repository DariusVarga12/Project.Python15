from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description provided.')  # Set your desired default value here

    def __str__(self):
        return self.name

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    recurrence = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f"Appointment for {self.service.name} on {self.appointment_date} at {self.appointment_time}"
