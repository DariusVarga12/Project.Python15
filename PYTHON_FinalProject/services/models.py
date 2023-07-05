from django.db import models


class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    recurrence = models.CharField(max_length=10)
    email = models.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f"Appointment for {self.service.name} on {self.appointment_date} at {self.appointment_time}"
