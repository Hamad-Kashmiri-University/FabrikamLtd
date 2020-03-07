from django.urls import path, include
from . import views
from .views import SessionListView, BookingCreateView, BookingView

urlpatterns = [
    path('', SessionListView.as_view(), name='Bookings'), #replace with views.home
    #path('detail/', views.detail, name='Booking-details'),
    #path('session/<int:pk>/',BookingCreateView.as_view(), name='details')
    path('session/<int:pk>/', views.BookingView, name='details')


]