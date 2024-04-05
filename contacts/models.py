from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from listings.models import Listing

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

class Order(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    email = models.CharField(max_length=100)

    class Status(models.TextChoices):
      IN_STOREHOUSE = "IN_STOREHOUSE"
      SHIPPED = "SHIPPED"
      ARRIVED = "ARRIVED"
    
    discount = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    status = models.CharField(max_length=13, choices=Status.choices, default=Status.IN_STOREHOUSE)
    
    purchase_date = models.DateTimeField(auto_now_add=True)

    arrival_date = models.DateTimeField(default=datetime.now)
      

    def __str__(self):
        return f'{self.listing.title} purchased by {self.customer}'
