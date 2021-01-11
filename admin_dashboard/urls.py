from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'admin_dashboard'

urlpatterns = [
    path('admin_user_registration/', RegisterAdminUserApiView.as_view()),
    path('admin_user_list/', ListAdminUserApiView.as_view()),
    path('admin_user_list/<id>/', ListAdminUserApiView.as_view()),
    path('update_admin_user/', UpdateAdminUserApiView.as_view()),
    path('delete_admin_user/<id>/', DeleteAdminUserApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    path('dashboard/', AdminDashboardApiView.as_view()),
]
