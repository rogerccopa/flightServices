from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
    
    # A custom validator should be of pattern: validate_<fieldName>
    # all custom validators are invoked when called: <mySerializer>.is_valid()
    def validate_flightNumber(self, flightNumber):
        if (re.match("^[a-zA-Z0-9]*$", flightNumber) == None):
            raise serializers.ValidationError("Invalid flight number. Make sure it is alphanumeric")
        return flightNumber

    # this method 'validate' is general for all fields (not just one in particular)
    def validate(self, data):
        # do validations here
        print(data['flightNumber'])
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
