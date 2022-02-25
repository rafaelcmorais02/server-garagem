from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user.models import NewUser
from user.serializers import UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        user = NewUser.objects.all()
        user_serializer = UserSerializer(
            user, many=True)
        resp = {
            'data': user_serializer.data,
            'userId': request.user.id
        }
        return Response(resp)
