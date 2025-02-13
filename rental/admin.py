from django.contrib import admin
from .models import Car, RentalLocation, Rental

admin.site.register(Car)
admin.site.register(RentalLocation)
admin.site.register(Rental)
