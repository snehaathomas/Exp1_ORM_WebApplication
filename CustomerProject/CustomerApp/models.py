from django.db import models
from django.contrib import admin

# Create your models here.
class Customer(models.Model):
    c_id=models.IntegerField(help_text="Enter Customer ID: ")
    c_name=models.CharField(max_length=100,help_text="Enter Customer Name: ")
    dob=models.DateField(help_text="Enter Date of Birth: ")
    no=models.IntegerField(help_text="Enter Contact Number: ")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['c_id', 'c_name', 'dob', 'no']

