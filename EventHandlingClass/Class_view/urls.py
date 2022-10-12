from django.urls import path
from .import views

urlpatterns=[ 
    path('event/',views.EventAPIView.as_view()),
    path('details/<int:id>',views.EventDetails.as_view())
]