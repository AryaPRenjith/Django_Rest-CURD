from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializer import EventSerializer
from .models import Event

# Create your views here.

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=EventSerializer
    queryset=Event.objects.all()

    def get(self,request):
        return self.list(request)