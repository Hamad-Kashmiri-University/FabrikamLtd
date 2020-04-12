from django.contrib import admin
from django.urls import path, include
from .  import views  # referncing views from user to call registerhtml
from django.contrib.auth import views as auth_views  #importing b-in django views for login and logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  #  path('', views.home, name="Home"),
    path('', views.home, name='Home'),
    path('about', views.about, name='About'),
    path('terms', views.terms, name='Terms'),
    path('privacy', views.privacy, name='Privacy')
    ]