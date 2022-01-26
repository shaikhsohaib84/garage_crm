from pyexpat import model
from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(null=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    ph_no = models.IntegerField(blank=False, null=False)
    address = models.TextField()
    class Meta:
        db_table = 'Customer'
    
    def __str__(self):
        return self.id

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    number_plate = models.CharField(null=False, unique=True, max_length=10)
    brand = models.TextField(null=False, blank=False)
    model_name = models.TextField(null=True, blank=True)
    chassis_no = models.CharField(blank=True, unique=True, max_length=20)
    engine_no = models.CharField(blank=True, unique=True, max_length=20)
    km = models.IntegerField(null=True, blank=True)
    due_km = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Vehicle'
    
    def __str__(self):
        return self.id

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.TextField() # Implies to specific module/part like engine, 
    serivce_desc = models.TextField()
    service_price = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'Service'
    
    def __str__(self):
        return self.id

class SubService(models.Model):
    id = models.AutoField(primary_key=True)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service_desc = models.TextField()

    class Meta:
        db_table = 'SubService'

    def __str__(self):
        return self.id

class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    bill_date = models.DateTimeField(auto_now_add=True)
    bill_amount = models.FloatField()

    class Meta:
        db_table = 'Billing'

    def __str__(self):
        return self.id

class Mapper(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vechileId = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    billId = models.ForeignKey(Billing, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Mapper'
    
    def __str__(self):
        return self.id