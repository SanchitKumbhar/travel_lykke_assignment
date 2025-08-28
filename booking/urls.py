from django.contrib import admin
from django.urls import path,include
from booking import views

urlpatterns = [
    path("booking-form/<int:id>",views.render_booking,name="booking-form"),
    path("booking-form/confirm",views.confirm,name="booking-confirm"),
    path("client-bookings",views.client_bookings,name="client-bookings"),
]
