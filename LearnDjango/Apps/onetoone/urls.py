from django.urls import path
from Apps.onetoone import views

urlpatterns = [
    path('', views.index, name='index-onetoone')
]
