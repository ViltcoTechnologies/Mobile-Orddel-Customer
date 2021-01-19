from django.urls import path
from django.contrib.auth import views as auth_views
from payment.views import *
from .views import *

app_name = 'order'

urlpatterns = [
    # CRUD of Order
    # Create
    path('create_cart/', CreateCartApiView.as_view(), name='create_cart'),
    path('add_to_cart/', CartProductsApiView.as_view(), name='add_to_cart'),
    # Read
    # path('clients_list/', ListClientsApiView.as_view(), name='list_clients'),
    # path('clients_list/<id>/', ListClientsApiView.as_view(), name='list_clients'),
    # # Update
    # path('update_client/', UpdateClientApiView.as_view(), name='update_client'),
    # # Delete
    # path('delete_client/<id>/', DeleteClientApiView.as_view(), name='delete_client'),

]
