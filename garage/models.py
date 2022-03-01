
from django.db import models
from user.models import NewUser


class Garage(models.Model):
    garage_name = models.CharField(max_length=254)
    user = models.ForeignKey(
        NewUser, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.garage_name
