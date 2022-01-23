from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    ph_no = models.IntegerField(max_length=10, blank=False, null=False)
    address = models.TextField()
    area = models.TextField()

    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.id


class vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    number_plate = models.CharField(unique=True, max_length=10)
    km = models.IntegerField(null=True, blank=True)
    due_km = models.IntegerField(null=True, blank=True)
    brand = models.TextField(null=False)
    model_name = models.TextField(null=False)
    chassis_no = models.TextField(unique=True)
    engine_no = models.TextField(unique=True)

    class Meta:
        db_table = 'vehicle'
    
    def __str__(self):
        return self.id

class service(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=100)
    serivce_desc = models.TextField()
    service_price = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'service'
    
    def __str__(self):
        return self.id

class billing(models.Model):
    id = models.AutoField(primary_key=True)
    bill_date = models.DateTimeField(auto_now_add=True)
    bill_amount = models.FloatField()

    class Meta:
        db_table = 'billing'

    def __str__(self):
        return self.id
    
class mapper(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(user, on_delete=models.CASCADE)
    vechileId = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    serviceId = models.ForeignKey(service, on_delete=models.CASCADE)
    billId = models.ForeignKey(billing, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mapper'
    
    def __str__(self):
        return self.id