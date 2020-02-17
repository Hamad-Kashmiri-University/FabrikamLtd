from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Bookings'),
    path('detail/', views.detail, name='Booking-details'),
]