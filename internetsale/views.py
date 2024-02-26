from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from internet.models import Internet
from internet.serializers import InternetSerializer
from internetsale.models import InternetSale
from django.db import models
from django.db.models import Sum
from .serializers import InternetSaleSerializer

@api_view(['POST'])
def internet_buy(request):
    if request.method == 'POST':
        # serializer = InternetSerializer(id=request.id)
        print(request.data.get('internet_id'))
        internet = Internet.objects.filter(id=request.data.get('internet_id'))[0]
        print(internet)
        if internet:
            phone_number = request.data.get('phone_number', None)
            if phone_number:
                today = date.today()
                total_price_today = InternetSale.objects.filter(phone_number=phone_number, created_at=today).aggregate(total_price=models.Sum('price'))['total_price']
                if total_price_today and total_price_today + internet.price > 500000:
                    return Response("Exceeded maximum purchase limit for today.", status=status.HTTP_400_BAD_REQUEST)
                
                internet_sale = InternetSale.objects.create(internet=internet, phone_number=phone_number, price=internet.price)
                serializer = InternetSaleSerializer(internet_sale)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Phone number has been not found.", status=status.HTTP_400_BAD_REQUEST)
        return Response("Internet has been not found.", status=status.HTTP_400_BAD_REQUEST)

