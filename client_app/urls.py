from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'client_app'


urlpatterns = [
    # CRUD of Clients
    path('client_registration/', ClientRegisterApiView.as_view(), name='create_client'),
    path('client_registration_v2/', ClientRegisterV2ApiView.as_view(), name='create_client'),
    path('clients_list/', ListClientsApiView.as_view(), name='list_clients'),
    path('clients_list/<id>/', ListClientsApiView.as_view(), name='list_clients'),
    path('update_client/', UpdateClientApiView.as_view(), name='update_client'),
    path('delete_client/<id>/', DeleteClientApiView.as_view(), name='delete_client'),
    path('upload_client_logo/', ClientLogoUploadAPIView.as_view(), name='upload_client_logo'),

    # CRUD of Business Details
    path('insert_business/', BusinessDetailInsertApiView.as_view(), name='insert_business_details'),
    path('list_business/', ListBusinessDetailsApiView.as_view(), name='list_business_details'),
    path('list_business/<id>/', ListBusinessDetailsApiView.as_view(), name='list_business_details/<id>'),
    path('list_business/client/<id>/', ListClientBusinessDetailsApiView.as_view(), name='list_business_details/client/<id>'),
    path('update_business/', UpdateBusinessApiView.as_view(), name='update_business_details'),
    path('delete_business/<id>/', DeleteBusinessApiView.as_view(), name='delete_business/<id>'),

    # Business Details APIs v2
    path('business_details/', BusinessDetailInsertGeneric.as_view(), name='insert_business_details'),

    # CRUD of Shipment Address
    path('insert_shipment/', ShipmentAddressCreateApiView.as_view(), name='insert_shipment'),
    path('list_shipment_address/', ListShipmentAddressApiView.as_view(), name='list_shipment_address'),
    path('list_shipment_address/<id>/', ListShipmentAddressApiView.as_view(), name='list_shipment_address/<id>'),
    path('list_shipment_address/client/<id>/', ListClientShipmentAddressApiView.as_view(),name='list_shipment_address/client/<id>'),
    path('update_shipment_add/', UpdateShipmentAddressApiView.as_view(), name='update_shipment_add'),
    path('delete_shipment_add/<id>/', DeleteShipmentAddressApiView.as_view(), name='delete_shipment_add'),

    # CRUD of Bank Details
    path('create_bank_details/', BankDetailsCreateApiView.as_view(), name='create_bank_details'),
    path('update_bank_details/', BankDetailsUpdateApiView.as_view(), name='update_bank_details'),
    path('list_bank_details/', ListBankDetailsApiView.as_view(), name='list_bank_details'),
    path('list_bank_details/<id>/', ListBankDetailsApiView.as_view(), name='list_bank_details/<id>'),
    path('list_bank_details/client/<id>/', ListClientBankDetailsApiView.as_view(),
         name='list_bank_details/client/<id>'),
    path('delete_bank_details/<id>/', DeleteBankDetailsApiView.as_view(), name='delete_bank_details'),

    # CRUD of Packages
    path('create_package/', PackageCreateApiView.as_view(), name='create_package'),
    path('update_package/', PackageUpdateApiView.as_view(), name='update_package'),
    path('list_packages/', ListPackagesApiView.as_view(), name='list_packages'),
    path('list_packages/<id>/', ListPackagesApiView.as_view(), name='list_packages/<id>'),
    path('list_clients/package/<id>/', ListClientPackagesApiView.as_view(),
         name='list_clients/package/<id>'),
    path('delete_package/<id>/', DeletePackageApiView.as_view(), name='delete_package'),

    # Admin Approval
    path('update_approval_status/', UpdateClientApprovalStatus.as_view()),
    path('approval_list/', PendingApprovalListApiView.as_view()),

    # Login
    path('client_login/', ClientLogin.as_view()),

    # Client home screen Dashboard
    path('client_dashboard/<id>/', ClientDashboardApiView.as_view()),
]
