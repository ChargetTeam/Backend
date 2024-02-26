"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from internet.views import internet_list
from chargesale.views import charge_buy
from internetsale.views import internet_buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/internet/', internet_list, name='internet-list'),
    path('api/internet-buy/', internet_buy, name='internet-buy'),
    path('api/charge-buy/', charge_buy, name='charge-buy'),
]
