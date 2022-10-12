from django.db import models

# Create your models here.

class Event(models.Model):
    Event_Name=models.CharField(max_length=100)
    Participent_Name=models.CharField(max_length=100)
    Participent_Address=models.CharField(max_length=100)

    def __str__(self):
        return self.Event_Name