from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyView.as_view(), name='index-classbasedview')
]
