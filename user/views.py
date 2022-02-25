from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user.models import NewUser
from user.serializers import UserSerializer, UserRegisterSerializer


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
            return Response(resp)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = NewUser.objects.get(pk=pk)
        user_serializer = UserSerializer(user)
        if user_serializer.data['id'] == request.user.id:
            resp = {
                'data': user_serializer.data
            }
        else:
            resp = {
                'data': 'Você não tem permissão de ver usuários diferentes do seu'
            }
        return Response(resp)
