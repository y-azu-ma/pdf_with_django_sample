from django.contrib import admin

# Register your models here.
from .models import CustomUser, OrderInfo

admin.site.register(CustomUser)
admin.site.register(OrderInfo)