from django.urls import path
from .views import rental_dashboard

urlpatterns = [
    path('dashboard/', rental_dashboard, name='rental_dashboard'),
]
