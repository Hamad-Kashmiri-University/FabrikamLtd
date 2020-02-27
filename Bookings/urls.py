from django.urls import path, include
from . import views
from .views import SessionListView, SessionDetailView

urlpatterns = [
    path('', SessionListView.as_view(), name='Bookings'), #replace with views.home
    #path('detail/', views.detail, name='Booking-details'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='details')

]