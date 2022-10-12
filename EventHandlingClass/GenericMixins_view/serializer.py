from dataclasses import fields
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['id','Event_Name','Participent_Name','Participent_Address']