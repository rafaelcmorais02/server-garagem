from django.urls import path
from garage.views import GarageRegisterView, GarageView, VehicleRegisterView, VehicleView, VehicleDetailView
urlpatterns = [
    path('register', GarageRegisterView.as_view()),
    path('', GarageView.as_view()),
    path('vehicle/register', VehicleRegisterView.as_view()),
    path('vehicles', VehicleView.as_view()),
    path('vehicle/update/<int:pk>', VehicleDetailView.as_view()),
]
