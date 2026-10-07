from rest_framework import serializers


class TurfBookingSerializer(serializers.Serializer):

    customer_name = serializers.CharField()

    phone = serializers.CharField()

    turf_name = serializers.CharField()

    booking_date = serializers.DateField()

    booking_time = serializers.TimeField(read_only=True)

    duration = serializers.IntegerField()

    problem = serializers.CharField()

    created_at = serializers.DateTimeField(read_only=True)