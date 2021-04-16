from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'delivery_app'

urlpatterns = [
    # Delivery Person API Routes
    path('delivery_person_registration/', RegisterDeliveryPersonApiView.as_view()),
    path('delivery_person_registration_v2/', RegisterDeliveryPersonApiViewV2.as_view()),
    path('delivery_person_list/', ListDeliveryPersonApiView.as_view()),
    path('delivery_person_list/<id>/', ListDeliveryPersonApiView.as_view()),
    path('update_delivery_person/', UpdateDeliveryPersonApiView.as_view()),
    path('delete_delivery_person/<id>/', DeleteDeliveryPersonApiView.as_view()),
    path('upload_delivery_person_logo/', DeliveryPersonLogoUploadAPIView.as_view(), name='upload_client_logo'),
    path('get_delivery_person_logo/<id>/', DeliveryPersonLogoUploadAPIView.as_view(), name='get_client_logo'),


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

    # ------------------------------------------------------------------------------------------------------------------

    # Business API Routes
    path('insert_business/', BusinessDetailInsertApiView.as_view(), name='insert_business_details'),
    path('list_business/', ListBusinessDetailsApiView.as_view(), name='list_business_details'),
    path('list_business/<id>/', ListBusinessDetailsApiView.as_view(), name='list_business_details/<id>'),
    path('list_business/delivery_person/<id>/', ListDeliveryPersonBusinessDetailsApiView.as_view(),
         name='list_business_details/delivery_person/<id>'),
    path('update_business/', UpdateBusinessApiView.as_view(), name='update_business_details'),
    # Delete
    path('delete_business/<id>/', DeleteBusinessApiView.as_view(), name='delete_business/<id>'),

    # ------------------------------------------------------------------------------------------------------------------

    # Bank Details API Routes
    path('create_bank_details/', BankDetailsCreateApiView.as_view(), name='create_bank_details'),
    path('update_bank_details/', BankDetailsUpdateApiView.as_view(), name='update_bank_details'),
    path('list_bank_details/', ListBankDetailsApiView.as_view(), name='list_bank_details'),
    path('list_bank_details/<id>/', ListBankDetailsApiView.as_view(), name='list_bank_details/<id>'),
    path('list_bank_details/delivery_person/<id>/', ListDeliveryPersonBankDetailsApiView.as_view(),
         name='list_bank_details/delivery_person/<id>'),
    path('delete_bank_details/<id>/', DeleteBankDetailsApiView.as_view(), name='delete_bank_details'),

    # ------------------------------------------------------------------------------------------------------------------

    # Package API Routes
    path('create_package/', PackageCreate.as_view(), name='create_package'),
    path('retrieve_update_delete_package/', RetrieveUpdateDestroyPackage.as_view(), name='create_package'),
    path('retrieve_update_delete_package/<int:id>/', RetrieveUpdateDestroyPackage.as_view(), name='create_package'),
    path('create_package/', PackageCreateApiView.as_view(), name='create_package'),
    path('update_package/', PackageUpdateApiView.as_view(), name='update_package'),
    path('list_packages/', ListPackagesApiView.as_view(), name='list_packages'),
    path('list_packages/<id>/', ListPackagesApiView.as_view(), name='list_packages/<id>'),
    path('list_delivery_person/package/<id>/', ListDeliveryPersonPackagesApiView.as_view(),
         name='list_delivery_person/package/<id>'),
    path('delete_package/<id>/', DeletePackageApiView.as_view(), name='delete_package'),

    # ------------------------------------------------------------------------------------------------------------------

    path('update_approval_status/', UpdateDeliveryPersonApprovalStatus.as_view()),
    path('approval_list/', PendingApprovalListApiView.as_view()),

    # Login
    path('delivery_person_login/', DeliveryPersonLogin.as_view()),

    # Delivery Person home screen Dashboard
    path('delivery_person_dashboard/<id>/', DeliveryPersonDashboardApiView.as_view()),

    # Incoming order
    path('update_order_status/', UpdateDeliveryPersonOrderApiView.as_view())
]
