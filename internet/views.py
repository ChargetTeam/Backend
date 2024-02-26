from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Internet
from .serializers import InternetSerializer

@api_view(['GET'])
def internet_list(request):
    if request.method == 'GET':
        internet_packages = Internet.objects.all()
        serializer = InternetSerializer(internet_packages, many=True)
        return Response(serializer.data)