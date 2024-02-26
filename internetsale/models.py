from django.db import models
from internet.models import *

class InternetSale(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    internet = models.ForeignKey(Internet, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}"
