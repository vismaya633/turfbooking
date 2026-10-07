from rest_framework import serializers
from .models import TurfBooking


class TurfBookingSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    customer_name = serializers.CharField()

    turf_name = serializers.CharField()

    sport = serializers.ChoiceField(
        choices=TurfBooking.TURF_OPTIONS
    )

    booking_date = serializers.IntegerField()

    booking_time = serializers.IntegerField()

    duration = serializers.IntegerField()

    amount = serializers.IntegerField()


    def validate(self, validated_data):

        duration = validated_data.get("duration")

        if duration <= 0:
            raise serializers.ValidationError(
                "Invalid duration, duration > 0"
            )

        amount = validated_data.get("amount")

        if amount <= 0:
            raise serializers.ValidationError(
                "Invalid amount, amount > 0"
            )

        return validated_data
    

class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()