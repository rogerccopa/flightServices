from django.contrib import admin
from django.urls import path, include
from flightApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightServices/', include(router.urls)),
    path('flightServices/findFlights', views.find_flights),
    path('flightServices/saveReservation', views.save_reservation)
]
