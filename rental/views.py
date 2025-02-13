from django.shortcuts import render
from .models import Rental
from django.db.models import Avg

def rental_dashboard(request):
    successful_rentals = Rental.objects.filter(payment='successful')
    unsuccessful_rentals = Rental.objects.filter(payment='not yet')
    average_price = Rental.objects.filter(payment='successful').aggregate(Avg('sale_price'))['sale_price__avg']

    context = {
        'successful_rentals': successful_rentals,
        'unsuccessful_rentals': unsuccessful_rentals,
        'average_price': average_price,
    }
    return render(request, 'rental/dashboard.html', context)
