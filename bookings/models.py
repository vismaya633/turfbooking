from django.db import models
from my_app.models import TurfBooking
# Create your models here.

class TurfBooking(models.Model):

    customer_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    turf_name = models.ForeignKey(TurfBooking,on_delete=models.CASCADE)

    booking_date = models.DateField()

    booking_time = models.TimeField(
        editable=False,
        null=True
    )

    duration = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name