from django.shortcuts import render
from .models import TravelOptions
from django.core import serializers
from django.http import JsonResponse
import json 
# Create your views here.
def render_travel_options(request):
    return render(request,"travel_options.html")

def process_travel_options(request):
    if request.method == "POST":
        # Get the JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
            
        travel_type = data.get("type")
        source = data.get("source")
        destination = data.get("destination")
        date = data.get("date")
        time = data.get("time")

        print(date, time, travel_type, source, destination)

        # Query the database
        obj = TravelOptions.objects.filter(
            travel_type=travel_type,
            source=source,
            destination=destination,
            date=date,
            time=time
        )
        
        # Corrected line: deserialize the JSON string into a Python object
        # and then pass it to JsonResponse
        serialized_data = serializers.serialize("json", obj)
        data = json.loads(serialized_data)
        
        print(data)
        return JsonResponse(data, safe=False)