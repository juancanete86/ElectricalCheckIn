from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    """User information"""
    id_card = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=30)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])

class Bill(models.Model):
    identifier = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(User)
    bill_date = models.DateTimeField(default=timezone.now)
    amount_price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    taxes = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    power_consumed = models.IntegerField(default=0, validators=[MinValueValidator(0)])
