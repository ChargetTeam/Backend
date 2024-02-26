# views.py
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChargeSale
from .serializers import ChargeSaleSerializer
from django.db import models

@api_view(['POST'])
def charge_buy(request):
    if request.method == 'POST':
        simcard_class = request.data.get('simcard_class', None)
        amount = request.data.get('amount', None)
        simcard_type = request.data.get('simcard_type', None)
        phone_number = request.data.get('phone_number', None)
        
        if not all([simcard_class, amount, simcard_type, phone_number]):
            return Response("Missing required fields.", status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the phone number has already bought charge for today
        today = date.today()
        total_price_today = ChargeSale.objects.filter(phone_number=phone_number, created_at=today).aggregate(total_price=models.Sum('amount'))['total_price']
        if total_price_today and total_price_today + float(price) > 500000:
            return Response("Exceeded maximum purchase limit for today.", status=status.HTTP_400_BAD_REQUEST)
        
        # Create ChargeSale object
        charge = ChargeSale.objects.create(simcard_class=simcard_class, amount=amount, simcard_type=simcard_type, phone_number=phone_number)
        serializer = ChargeSaleSerializer(charge)
        return Response(serializer.data, status=status.HTTP_201_CREATED)