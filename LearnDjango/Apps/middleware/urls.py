from django.urls import path
from Apps.middleware import views

urlpatterns = [
    path('', views.index, name='index-middleware')
]
