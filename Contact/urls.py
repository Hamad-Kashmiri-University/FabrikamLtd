from django.urls import path, include
from Contact import views

urlpatterns = [
    path('contact/', views.contact, name='Contact'),
]