from django.contrib import admin
from django.urls import path,include
from traveloptions import views
urlpatterns = [
    path("travel-options",views.render_travel_options,name="travel-options"),
    path("check-travel-options",views.process_travel_options,name="check-travel-options")
]