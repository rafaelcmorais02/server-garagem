from rest_framework.authtoken import views
from django.urls import path
from user.views import UserView, UserDetailView, UserRegisterView
from user.AuthTokenView import CustomAuthToken
urlpatterns = [
    # Rota parar recebimento de token (usada no front-end)
    path('api-token-auth/', CustomAuthToken.as_view()),
    # Rota para listar usuários
    path('', UserView.as_view()),
    # Rota para registro de usuários (usada no front-end)
    path('register', UserRegisterView.as_view()),
    # Rota para a busca de um único usuário
    path('<int:pk>', UserDetailView.as_view())
]
