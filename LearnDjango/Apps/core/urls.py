from django.urls import path
from Apps.core import views



urlpatterns = [
    path('', views.index, name='index-core'),
    
]
