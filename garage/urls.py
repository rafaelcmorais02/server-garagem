from django.urls import path
from garage.views import GarageRegisterView, GarageView, VehicleRegisterView, VehicleView, VehicleDetailView, GarageDetailView
urlpatterns = [
    # Rota para registro de garagens (usada no front-end)
    path('register', GarageRegisterView.as_view()),
    # Rota para retorno de todas as garagens (usada no front-end)
    path('', GarageView.as_view()),
    # Rota para remover garagem (usada no front-end)
    path('delete/<int:pk>', GarageDetailView.as_view()),
    # Rota para registrar veículo (usada no front-end)
    path('vehicle/register', VehicleRegisterView.as_view()),
    # Rota para listar todos os veívulos (usada no front-end)
    path('vehicles', VehicleView.as_view()),
    # Rota para atualizar um veículo
    path('vehicle/update/<int:pk>', VehicleDetailView.as_view()),
]
