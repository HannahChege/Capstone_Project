from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from .models import food,Restaurant
# Register your models here.
admin.site.register(food)
admin.site.register(Restaurant)
 