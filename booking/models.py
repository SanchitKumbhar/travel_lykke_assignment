from django.db import models
from django.conf import settings  # Import the User model
from traveloptions.models import TravelOptions  # Adjust the path as needed

class Booking(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    travel_option = models.ForeignKey(TravelOptions, on_delete=models.CASCADE, related_name='TravelOptions')
    number_of_seats = models.PositiveIntegerField()  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CONFIRMED')

    def __str__(self):
        return f"{self.travel_option.travel_type} from {self.travel_option.source} to {self.travel_option.destination} ({self.number_of_seats} seats)"

