from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from my_app.models import TurfBooking
from myapp_v2.serializers import TurfBookingSerializer,UserSerializer
# Create your views here.
class TurfBookingListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):

        qs = TurfBooking.objects.all()

        serializer_instance = TurfBookingSerializer(
            qs,
            many=True
        )

        return Response(
            data=serializer_instance.data
        )

    def post(self, request):

        form_data = request.data

        serializer_instance = TurfBookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            TurfBooking.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)


class TurfBookingRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk=None):

        qs = TurfBooking.objects.get(id=pk)

        serializer_instance = TurfBookingSerializer(qs)

        return Response(serializer_instance.data)

    def put(self, request, pk=None):

        form_data = request.data

        serializer_instance = TurfBookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            TurfBooking.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self, request, pk=None):

        qs = TurfBooking.objects.get(id=pk)

        serializer_instance = TurfBookingSerializer(qs)

        qs.delete()

        return Response(serializer_instance.data)
    
class AdminCreateView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)