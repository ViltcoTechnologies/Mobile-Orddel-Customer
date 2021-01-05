from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'client_app'

urlpatterns = [
    # Create
    path('create/', ClientRegisterApiView.as_view(), name='create'),
    # Read
    path('list/', ListClientsApiView.as_view(), name='list'),
    # Update
    path('update/', UpdateClientApiView.as_view(), name='update'),
    # Delete
    path('delete/', DeleteClientApiView.as_view(), name='delete'),


]
