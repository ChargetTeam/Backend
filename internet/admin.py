from django.contrib import admin
from .models import Internet
 
@admin.register(Internet)
class InternetAdmin(admin.ModelAdmin):
  list_data = ["id"]
#   list_display = [field.name for field in Internet._meta.get_fields()]
