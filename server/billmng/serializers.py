from rest_framework import serializers
from models import Bill, User

class BillSerializer(serializers.ModelSerializer):
    """Serializer to represent the Bill model"""
    class Meta:
        model = Bill
        fields = ("identifier", "user", "bill_date", "amount_price", "taxes", "power_consumed")


class UserSerializer(serializers.ModelSerializer):
    """Serializer to represent the Bill model"""
    class Meta:
        model = User
        fields = ("id_card", "username", "password", "first_name", "last_name", "address", "city",
                  "province", "country", "zipcode", "age")
