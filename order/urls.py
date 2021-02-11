from django.urls import path
from django.contrib.auth import views as auth_views
from payment.views import *
from .views import *

app_name = 'order'

urlpatterns = [
    # CRUD of Cart
    path('create_order_box/', CreateOrderBoxApiView.as_view(), name='create_cart'),  # Create
    path('list_order_box/', ListOrderBoxApiView.as_view()),  # Read All
    path('list_order_box/<id>/', ListOrderBoxApiView.as_view()),  # Read By ID
    path('update_order_box/', UpdateOrderBoxApiView.as_view()),  # Update
    path('delete_order_box/<id>/', DeleteOrderBoxApiView.as_view()),  # Delete

    # CRUD of Add to Cart
    path('add_to_order_box/', AddOrderBoxProductsApiView.as_view(), name='add_to_cart'),
    path('list_all_order_box_products/', ListOrderBoxProductsApiView.as_view(), name='list_all_cart_products'),
    path('list_order_box_products/<id>/', ListOrderBoxProductsApiView.as_view(), name='list_cart_products'),
    path('update_order_box_product/', UpdateOrderBoxProductsApiView.as_view(), name='update_cart_products'),
    path('delete_order_box_product/<id>/', DeleteOrderBoxProductsApiView.as_view(), name='delete_cart_products/<id>/'),

    # CRUD of Order
    path('create_order/', CreateOrderApiView.as_view(), name='create_order'),
    path('update_order/', UpdateOrderApiView.as_view(), name='update_order'),
    path('list_order/', ListOrderApiView.as_view(), name='list_order'),
    path('list_order/<id>/', ListOrderApiView.as_view(), name='list_order/<id>/'),
    path('delete_order/<int:pk>', DeleteOrderApiView.as_view(), name='delete_order/'),

    # Get PO number
    path('get_po_number/<id>/', GetPONumberAPIView.as_view(), name='get_po_number'),
    path('list_assigned_orders/', ListOrdersAssignedAPIView.as_view(), name='list_assigned_orders'),

]
