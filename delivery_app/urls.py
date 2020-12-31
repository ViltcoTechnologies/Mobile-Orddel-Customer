from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'delivery_app'

urlpatterns = [
    path('create/', DeliveryPersonApiView.as_view()),
    # path('update/', ),
    # path('delete/', ),
    # path('list/', )
]
