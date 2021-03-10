from django.urls import path
from django.contrib.auth import views as auth_views
from payment.views import *

app_name = 'payment'

urlpatterns = [
    path('create_list_invoice/', ListCreateInvoice.as_view()),
    path('retrieve_update_destroy_invoice/<int:pk>', RetrieveUpdateDestroyInvoice.as_view()),
    path('get_invoice_number/<id>/', GetInvNumberAPIView.as_view()),
    path('get_delivery_note_number/<id>/', GetDeliveryNoteNumberAPIView.as_view()),
    path('add_delivery_note/', CreateDeliveryNote.as_view()),
    path('generate_invoice/<id>/', GenerateInvoiceAPIView.as_view()),
    path('view_invoice/<id>/', ViewInvoiceApiView.as_view()),
    path('generate_invoice_pdf/<id>/', GeneratePDFInvoiceAPIView.as_view()),




]
