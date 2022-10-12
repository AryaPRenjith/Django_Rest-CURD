from django.urls import path
from .import views

urlpatterns=[ 
    path('view/',views.GenericAPIView.as_view()),
    path('view/<int:id>',views.GenericAPIView.as_view())
]