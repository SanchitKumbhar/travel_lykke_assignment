from django.shortcuts import render
from django.http import  JsonResponse
from traveloptions.models import  TravelOptions
from .models import Booking
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def render_booking(request,id):
    instance=TravelOptions.objects.get(pk=id)



    print(instance)
    return render(request,"book_form.html",context={
        "travel_option" : instance
    })

def confirm(request):
        if request.method == "POST":
            data = json.loads(request.body)
            
            print(data)
            travel_option_instance = TravelOptions.objects.get(pk=int(data.get("travel_option_id")))
            booking = Booking.objects.create(
                user=request.user,
                travel_option=travel_option_instance,
                number_of_seats=data.get("seats"),
                total_price=data.get("total_price"),
                status='CONFIRMED'
                # Include other necessary fields from the form data
            )
            return JsonResponse({
                "status" : 201
            })
@login_required
def client_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "user_bookings.html", context={
        "bookings": bookings
    })
