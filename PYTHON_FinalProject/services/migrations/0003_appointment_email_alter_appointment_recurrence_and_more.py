# Generated by Django 4.2.2 on 2023-07-03 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_appointment_recurrence'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='recurrence',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
