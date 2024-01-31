from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_guests = models.IntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.FloatField()
    inventory = models.IntegerField() 

