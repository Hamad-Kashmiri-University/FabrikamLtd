from django.contrib import admin
from .models import Session, IndividualSession, Booking

admin.site.register(Session)

admin.site.register(IndividualSession)

admin.site.register(Booking)
