from rest_framework.authtoken import views
from django.urls import path
from user.views import UserView, UserDetailView
from user.AuthTokenView import CustomAuthToken
urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('', UserView.as_view()),
    path('<int:pk>', UserDetailView.as_view())
]
