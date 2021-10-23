from django.urls import path
from Apps.signals import views

urlpatterns = [
    path('', views.index, name='index-signals'),
    
]
