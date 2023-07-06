from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description provided.')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    last_name = models.CharField(max_length=100)
    recurrence = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.CharField(max_length=100, default=1)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
