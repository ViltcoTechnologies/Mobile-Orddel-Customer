from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'admin_dashboard'

urlpatterns = [
    path('create/', AdminDashboardApiView.as_view()),
    # path('update/', ),
    # path('delete/', ),
    # path('list/', )
]
