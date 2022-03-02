
from django.db import models
from user.models import NewUser


class Garage(models.Model):
    garage_name = models.CharField(max_length=254)
    user = models.ForeignKey(
        NewUser, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.garage_name


class Vehicle(models.Model):
    TYPES = (
            ('C', 'Carro'),
            ('M', 'Moto'),
    )
    type = models.CharField(choices=TYPES, max_length=1)
    model = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    garage = models.ForeignKey(
        Garage, related_name='garage', on_delete=models.CASCADE)

    def __str__(self):
        return self.model
