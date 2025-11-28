from django.contrib import admin
from .models import Customer, CustomerAdmin 
# Register your models here.
admin.site.register(Customer, CustomerAdmin)
