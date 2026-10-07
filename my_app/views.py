from django.shortcuts import render

from .models import TurfBooking

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers

# Create your views here.
class TurfBookingListCreateView(APIView):

    def get(self, request):

        qs = TurfBooking.objects.all().values()

        booking_list = list(qs)

        return Response(data=booking_list)


    def post(self, request):

        form_data = request.data

        sport = form_data.get("sport")

        if sport not in dict(TurfBooking.TURF_OPTIONS):
            raise serializers.ValidationError(
                sport + " is not a valid choice"
            )

        TurfBooking.objects.create(**form_data)

        return Response(data={"message": "created"})


class TurfBookingRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk=None):

        qs = TurfBooking.objects.filter(id=pk).values()

        booking_list = list(qs)

        return Response(data=booking_list)


    def put(self, request, pk=None):

        form_data = request.data

        TurfBooking.objects.filter(id=pk).update(**form_data)

        return Response(data={"message": "updated"})


    def delete(self, request, pk=None):

        TurfBooking.objects.get(id=pk).delete()

        return Response(data={"message": "deleted"})

