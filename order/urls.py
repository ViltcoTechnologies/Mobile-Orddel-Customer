from django.urls import path
from django.contrib.auth import views as auth_views
from payment.views import *
from .views import *

app_name = 'order'




urlpatterns = [
    # CRUD of Cart

    path('create_cart/', CreateCartApiView.as_view(), name='create_cart'),  # Create
    path('list_carts/', ListCartApiView.as_view()),  # Read All
    path('list_carts/<id>/', ListCartApiView.as_view()),  # Read By ID
    path('update_cart/', UpdateCartApiView.as_view()),  # Update
    path('delete_cart/<id>/', DeleteCartApiView.as_view()),  # Delete

    # CRUD of Add to Cart
    path('add_to_cart/', AddCartProductsApiView.as_view(), name='add_to_cart'),
    path('list_all_cart_products/', ListCartProductsApiView.as_view(), name='list_all_cart_products'),
    path('list_cart_products/<id>/', ListCartProductsApiView.as_view(), name='list_cart_products'),
    path('update_cart_products/', UpdateCartProductsApiView.as_view(), name='update_cart_products'),
    path('delete_cart_products/<id>/', DeleteCartProductsApiView.as_view(), name='delete_cart_products/<id>/'),


    path('create_order/', CreateOrderApiView.as_view(), name='create_order'),
    # Read
    # path('clients_list/', ListClientsApiView.as_view(), name='list_clients'),
    # path('clients_list/<id>/', ListClientsApiView.as_view(), name='list_clients'),
    # # Update
    # path('update_client/', UpdateClientApiView.as_view(), name='update_client'),
    # # Delete
    # path('delete_client/<id>/', DeleteClientApiView.as_view(), name='delete_client'),

]
