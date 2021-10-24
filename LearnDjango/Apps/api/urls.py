from django.urls import path
from .import views

urlpatterns = [
    path('', views.MyIndex.as_view(), name='index-api'),
    path('data/<int:pk>/', views.data, name='data')
]
