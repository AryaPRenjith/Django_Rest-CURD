from django.shortcuts import render
from .models import Event
from .serializer import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django .http import HttpResponse

# Create your views here.

class EventAPIView(APIView):

    def get(self,request):
        events=Event.objects.all()
        serializer=EventSerializer(events, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EventDetails(APIView):

    def get_object(self, id):

        try:

           return Event.objects.get(id=id)

        except Event.DoesNotExist:
        
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,id):
        eve=self.get_object(id)
        serializer=EventSerializer(eve)
        return Response(serializer.data)

    def put(self,request,id):

        eve=self.get_object(id)
        serializer=EventSerializer(eve,data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):

        eve=self.get_object(id)
        eve.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)




    
