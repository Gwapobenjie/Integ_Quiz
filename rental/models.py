from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.model})"

class RentalLocation(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_location = models.ForeignKey(RentalLocation, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, choices=[('not yet', 'Not Yet'), ('successful', 'Successful')])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.car.name} rented by {self.renter.username}"