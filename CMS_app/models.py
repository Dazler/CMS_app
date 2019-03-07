from django.conf import settings
from django.db import models
from django.utils import timezone


class Aircraft(models.Model):
    MSN = models.IntegerField(default=0)
    Harness_length = models.IntegerField(default=0)
    Gross_weight = models.IntegerField(default=0)
    Atmospheric_pressure = models.IntegerField(default=0)
    Room_temperature = models.IntegerField(default=0)
    Airport = models.TextField(default="Heaven")
    Fuel_Capacity_on_Left_Wing = models.IntegerField(default=0)
    Fuel_Capacity_on_Right_Wing = models.IntegerField(default=0)
    Fuel_Quantity_on_Left_Wing = models.IntegerField(default=0)
    Fuel_Quantity_on_Right_Wing = models.IntegerField(default=0)
    Maximum_Altitude_to_be_Reached = models.IntegerField(default=0)
    Flight_No = models.TextField(default="CR7")
    Flight_type = models.TextField(default="Based_on_button")

class NewsFeed(models.Model):
	HeadLine = models.TextField(default="Heaven")
	Content = models.TextField(default="Heaven")
    