from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django_email_verification import urls as mail_urls
from ordel.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # verifications
    path('email/', include(mail_urls)),
    path('resend_otp/', ResendOtpApiView.as_view()),
    path('verify_otp/', VerifyPhoneNumberApiView.as_view()),

    # Reset Password URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # Apps URLs
    path('client_app/', include("client_app.urls")),
    path('delivery_person/', include("delivery_app.urls")),
    path('order/', include("order.urls")),
    path('payment/', include("payment.urls")),
    path('product/', include("products.urls")),
    path('admin_app/', include("admin_dashboard.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




