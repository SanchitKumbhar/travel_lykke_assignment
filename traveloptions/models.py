from django.db import models
from django.utils import timezone


# Create your models here.
class TravelOptions(models.Model):
    TRAVEL_OPITONS=[
        ("A","Flight"),
        ("B","Train"),
        ("C","Bus")
    ]

    travelid = models.BigAutoField(primary_key=True)
    travel_type=models.CharField(choices=TRAVEL_OPITONS,default="C",max_length=10)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    price=models.IntegerField()
    available_seats=models.IntegerField()
    date = models.DateField()
    time=models.TimeField() 
    def __str__(self):
        return f"{self.get_travel_type_display()} from {self.source} to {self.destination}"