from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'admin_dashboard'

urlpatterns = [
    path('delivery_person_registration/', RegisterAdminUserApiView.as_view()),
    path('delivery_person_list/', ListAdminUserApiView.as_view()),
    path('delivery_person_list/<id>/', ListAdminUserApiView.as_view()),
    path('update_delivery_person/', UpdateAdminUserApiView.as_view()),
    path('delete_delivery_person/<id>/', DeleteAdminUserApiView.as_view()),
]
