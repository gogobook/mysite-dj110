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




    