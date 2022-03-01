from django.urls import path
from garage.views import GarageRegisterView, GarageView
urlpatterns = [
    path('register', GarageRegisterView.as_view()),
    path('', GarageView.as_view())
]
