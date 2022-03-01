from rest_framework.serializers import ModelSerializer
from .models import Garage, Vehicle


class GarageSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id', 'garage_name', 'user']


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type', 'model', 'color', 'garage']
