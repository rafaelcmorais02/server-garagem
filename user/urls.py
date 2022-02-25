from rest_framework.authtoken import views
from django.urls import path
from user.views import UserView, UserDetailView
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', UserView.as_view()),
    path('<int:pk>', UserDetailView.as_view())
]
