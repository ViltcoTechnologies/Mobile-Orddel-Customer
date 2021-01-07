from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'client_app'


urlpatterns = [
    # CRUD of Clients

    # Create
    path('client_registration/', ClientRegisterApiView.as_view(), name='create_client'),
    # Read
    path('clients_list/', ListClientsApiView.as_view(), name='list_clients'),
    path('clients_list/<id>/', ListClientsApiView.as_view(), name='list_clients'),
    # Update
    path('update_client/', UpdateClientApiView.as_view(), name='update_client'),
    # Delete
    path('delete_client/<id>/', DeleteClientApiView.as_view(), name='delete_client'),

    # CRUD of Business Details

    # Create
    path('insert_business/', BusinessDetailInsertApiView.as_view(), name='insert_business_details'),
    # Read
    path('list_business/', ListBusinessDetailsApiView.as_view(), name='list_business_details'),
    path('list_business/<id>/', ListBusinessDetailsApiView.as_view(), name='list_business_details/<id>'),
    path('list_business/client/<id>/', ListClientBusinessDetailsApiView.as_view(), name='list_business_details/client/<id>'),
    # Update
    path('update_business/', UpdateBusinessApiView.as_view(), name='update_business_details'),
    # Delete
    path('delete_business/<id>/', DeleteBusinessApiView.as_view(), name='delete_business/<id>'),

    # CRUD of Shipment Address
    # Create
    path('insert_shipment/', ShipmentAddressCreateApiView.as_view(), name='insert_shipment'),
    # Read
    path('list_shipment_address/', ListShipmentAddressApiView.as_view(), name='list_shipment_address'),
    path('list_shipment_address/<id>/', ListShipmentAddressApiView.as_view(), name='list_shipment_address/<id>'),
    path('list_shipment_address/client/<id>/', ListClientShipmentAddressApiView.as_view(),name='list_shipment_address/client/<id>'),
    # Update
    path('update_shipment_add/', UpdateShipmentAddressApiView.as_view(), name='update_shipment_add'),
    # Delete
    path('delete_shipment_add/<id>/', DeleteShipmentAddressApiView.as_view(), name='delete_shipment_add'),

    # CRUD of Bank Details
    path('create_bank_details/', BankDetailsCreateApiView.as_view(), name='create_bank_details')
]
