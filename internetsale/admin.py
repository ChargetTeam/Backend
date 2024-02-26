from django.contrib import admin
from .models import InternetSale
 
@admin.register(InternetSale)
class InternetSaleAdmin(admin.ModelAdmin):
  list_display = [field.name for field in InternetSale._meta.get_fields()]
