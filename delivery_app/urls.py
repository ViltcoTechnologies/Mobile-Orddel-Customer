from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'delivery_app'

urlpatterns = [
    path('create/', RegisterDeliveryPersonApiView.as_view()),
    path('update/', UpdateDeliveryPersonApiView.as_view()),
    path('delete/', DeleteDeliveryPersonApiView.as_view()),
    path('list/', ListDeliveryPersonApiView.as_view()),
]
