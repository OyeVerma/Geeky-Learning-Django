from django.urls import path
from Apps.filters import views

urlpatterns = [
    path('', views.index, name='index-filters')
]
