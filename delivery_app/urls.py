from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'delivery_app'

urlpatterns = [
    # Delivery Person API Routes
    path('delivery_person_registration/', RegisterDeliveryPersonApiView.as_view()),
    path('delivery_person_list/', ListDeliveryPersonApiView.as_view()),
    path('delivery_person_list/<id>/', ListDeliveryPersonApiView.as_view()),
    path('update_delivery_person/', UpdateDeliveryPersonApiView.as_view()),
    path('delete_delivery_person/<id>/', DeleteDeliveryPersonApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Vehicle API Routes
    path('vehicle_registration/', RegisterVehicleApiView.as_view()),
    path('vehicle_list/', ListVehicleApiView.as_view()),
    path('vehicle_list/<id>/', ListVehicleApiView.as_view()),
    path('vehicle_list/delivery_person/<id>/', ListDeliveryPersonVehicleApiView.as_view()),
    path('update_vehicle/', UpdateVehicleApiView.as_view()),
    path('delete_vehicle/<id>/', DeleteVehicleApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Consolidated Purchase API Routes
    path('create_consolidated_purchase/', RegisterVehicleApiView.as_view()),
    path('consolidated_purchase_list/', ListVehicleApiView.as_view()),
    path('consolidated_purchase_list/<id>/', ListVehicleApiView.as_view()),
    path('consolidated_purchase_list/delivery_person/<id>/', ListDeliveryPersonVehicleApiView.as_view()),
    path('update_consolidated_purchase/', UpdateVehicleApiView.as_view()),
    path('delete_consolidated_purchase/<id>/', DeleteVehicleApiView.as_view()),
]
