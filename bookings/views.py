from django.shortcuts import render
from rest_framework.views import APIView
from bookings.models import TurfBooking
from bookings.serializers import TurfBookingSerializer

from rest_framework.response import Response

# Create your views here.
class TurfBookingListCreateView(APIView):

    def get(self, request):

        qs = TurfBooking.objects.all()

        serializer_instance = TurfBookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

