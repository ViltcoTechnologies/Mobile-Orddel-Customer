from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'admin_dashboard'

urlpatterns = [
    # Admin Dashboard API Routes
    path('admin_user_registration/', RegisterAdminUserApiView.as_view()),
    path('admin_user_list/', ListAdminUserApiView.as_view()),
    path('admin_user_list/<id>/', ListAdminUserApiView.as_view()),
    path('update_admin_user/', UpdateAdminUserApiView.as_view()),
    path('delete_admin_user/<id>/', DeleteAdminUserApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Orddel Dashboard API Routes
    path('dashboard/', AdminDashboardApiView.as_view()),
    path('order_graph/', OrderGraphApiView.as_view()),

    # ------------------------------------------------------------------------------------------------------------------

    # Approval Log API Routes
    path('create_client_approval_log/', CreateClientApprovalLog.as_view()),
    path('create_delivery_person_approval_log/', CreateDeliveryPersonApprovalLog.as_view()),
    path('admin_user_login/', AdminLogin.as_view()),

]
