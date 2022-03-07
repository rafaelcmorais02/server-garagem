from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import GarageSerializer, VehicleSerializer
from .models import Garage, Vehicle
from django.shortcuts import get_object_or_404


class GarageRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        garage_serializer = GarageSerializer(data=request.data)
        if garage_serializer.is_valid():
            garage_serializer.save()
            resp = {
                'message': 'garagem cadastrada com sucesso',
                'data': request.data
            }
            return Response(resp, status=201)
        else:
            return Response({'message': 'erro no cadastro da garagem'}, status=400)


class GarageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        garage = Garage.objects.all()
        user = request.query_params.get('user')
        if user is not None:
            garage = garage.filter(user=user)
            garage_serializer = GarageSerializer(garage, many=True)
            resp = {
                'data': garage_serializer.data,
            }
            return Response(resp)
        garage_serializer = GarageSerializer(garage, many=True)
        resp = {
            'data': garage_serializer.data,
        }
        return Response(resp)


class GarageDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        garage = get_object_or_404(Garage, pk=pk)
        garage.delete()
        return Response({
            'message': f'Garagem {pk} deletada com sucesso'
        })


class VehicleRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        vehicle_serializer = VehicleSerializer(data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            resp = {
                'message': 'Veículo cadastrada com sucesso',
                'data': request.data
            }
            return Response(resp, status=201)
        else:
            return Response({'message': 'erro no cadastro do veículo'}, status=400)


class VehicleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vehicle = Vehicle.objects.all()
        garage = request.query_params.get('garage')
        if garage is not None:
            vehicle = vehicle.filter(garage=garage)
            vehicle_serializer = VehicleSerializer(vehicle, many=True)
            resp = {
                'data': vehicle_serializer.data,
            }
            return Response(resp)
        vehicle_serializer = VehicleSerializer(vehicle, many=True)
        resp = {
            'data': vehicle_serializer.data,
        }
        return Response(resp)


class VehicleDetailView(APIView):
    def patch(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle_serializer = VehicleSerializer(
            vehicle, data=request.data, partial=True)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            resp = {
                'message': 'Veículo atualizado com sucesso',
                'data': request.data
            }
            return Response(resp, status=201)
        else:
            return Response({'message': 'erro na atualização do veículo'}, status=400)
