from rest_framework import serializers
from .models import ChargeSale

class ChargeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeSale
        fields = ('id', 'created_at', 'simcard_class', 'amount', 'simcard_type', 'phone_number')
