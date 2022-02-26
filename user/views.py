from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user.models import NewUser
from user.serializers import UserSerializer, UserRegisterSerializer
from user.permissions import IsAuthor


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        users = NewUser.objects.all()
        users_serializer = UserSerializer(
            users, many=True)
        resp = {
            'data': users_serializer.data,
            'userId': request.user.id
        }
        return Response(resp)

    def post(self, request):
        user_serializer = UserRegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            resp = {
                'message': 'usuário cadastrado com sucesso',
                'data': request.data
            }
            return Response(resp, status=201)
        else:
            return Response({'message': 'erro no cadastro do usuário'}, status=400)


class UserDetailView(APIView):
    permission_classes = [IsAuthor, ]

    def get(self, request, pk):
        user = get_object_or_404(NewUser, pk=pk)
        self.check_object_permissions(self.request, user)
        user_serializer = UserSerializer(user)
        resp = {
            'data': user_serializer.data
        }
        return Response(resp)
