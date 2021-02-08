from django.urls import path
from django.contrib.auth import views as auth_views
from payment.views import *

app_name = 'payment'

urlpatterns = [
    path('create_list_invoice/', ListCreateInvoice.as_view()),

]
