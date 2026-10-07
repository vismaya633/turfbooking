from django.db import models

# Create your models here.



class TurfBooking(models.Model):

    TURF_OPTIONS = (
        ("football", "Football"),
        ("cricket", "Cricket"),
        ("badminton", "Badminton"),
        ("other", "Other"),
    )

    customer_name = models.CharField(max_length=200)
    turf_name = models.CharField(max_length=200)
    sport = models.CharField(max_length=200,choices=TURF_OPTIONS,default="football")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.IntegerField()
    phone = models.IntegerField
    amount = models.IntegerField()

    def __str__(self):
        return self.customer_name