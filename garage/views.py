from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GarageSerializer
from .models import Garage
from user.serializers import UserSerializer


class GarageRegisterView(APIView):
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
    def get(self, request):
        garage = Garage.objects.all()
        garage_serializer = GarageSerializer(garage, many=True)
        resp = {
            'data': garage_serializer.data,
        }
        return Response(resp)
