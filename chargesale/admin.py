from django.contrib import admin
from .models import ChargeSale
 
@admin.register(ChargeSale)
class ChargeSaleAdmin(admin.ModelAdmin):
  list_display = [field.name for field in ChargeSale._meta.get_fields()]
