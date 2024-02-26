from django.db import models

class ChargeSale(models.Model):
    HAMRAHE_AVAL = 'HamraheAval'
    IRANCELL = 'Irancell'
    RIGHTEL = 'RighTel'
    
    CLASS_CHOICES = [
        (HAMRAHE_AVAL, 'HamraheAval'),
        (IRANCELL, 'Irancell'),
        (RIGHTEL, 'RighTel'),
    ]
    
    PERMANENT = 'Permanent'
    CREDIT = 'Credit'
    
    TYPE_CHOICES = [
        (PERMANENT, 'Permanent'),
        (CREDIT, 'Credit'),
    ]
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    simcard_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    simcard_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}"