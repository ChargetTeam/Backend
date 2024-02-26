from rest_framework import serializers
from .models import Internet

class InternetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internet
        fields = ('id', 'created_at', 'title', 'simcard_class', 'duration', 'size', 'price', 'simcard_type')
