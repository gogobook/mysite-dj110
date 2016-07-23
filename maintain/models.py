from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=200)
    itsmodel = models.CharField(max_length=200)
    producedYear = models.DateTimeField('produced years')
    pistonDisplacement = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200)

class Part(models.Model):
    partName = models.CharField(max_length=200)
    partNo = models.IntegerField(default=0)
    car = models.ForeignKey(car）
    category = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
<<<<<<< Updated upstream
=======
    price = models.IntegerField(default=0)

class Work(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

class Consumer(models.Model):
    name = models.CharField(max_length=200)
    phoneNo = models.IntegerField(default=0)
    car = models.ForeignKey(car）
    brandNo = models.CharField(max_length=200)

class Master(models.Model):
    name = models.CharField(max_length=200)

class WorkOrder(models.Model):
    date = models.DateField()
    consumer = models.ForeignKey()
    master = models.ForeignKey()
    part = models.ForeignKey()
    work = models.ForeignKey()
    totalprice = models.IntegerField(default=0)

>>>>>>> Stashed changes




    