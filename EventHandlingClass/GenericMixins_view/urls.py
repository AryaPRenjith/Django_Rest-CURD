from django.urls import path
from .import views


urlpatterns=[ 
    path('generic/',views.GenericAPIView.as_view())
]