from rest_framework import serializers
from .models import InternetSale

class InternetSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetSale
        fields = ['id', 'created_at', 'internet', 'price', 'phone_number']
