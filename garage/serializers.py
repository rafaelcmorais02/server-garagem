from rest_framework.serializers import ModelSerializer
from .models import Garage


class GarageSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = ['garage_name', 'user']
