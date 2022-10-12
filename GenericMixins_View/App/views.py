from urllib import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializer import EventSerializer
from .models import Event

# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin ):


    serializer_class=EventSerializer
    queryset=Event.objects.all()

    lookup_field='id'

    def get(self,request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request, id=None):
        return self.update(request, id)

    def delete(self, request,id):
        return self.destroy(request,id)

