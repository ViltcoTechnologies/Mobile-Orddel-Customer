from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django_email_verification import urls as mail_urls
from ordel.views import *
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', FCMDeviceAuthorizedViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Orddel APIs')
urlpatterns = [
    path('swagger/', schema_view),
    path('devices/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # verifications
    path('email/', include(mail_urls)),
    path('send_otp/', SendOTPAPIView.as_view()),
    path('resend_otp/', ResendOtpApiView.as_view()),
    path('verify_otp/', VerifyPhoneNumberApiView.as_view()),
    path('verify_otp_v2/', VerifyPhoneNumberV2ApiView.as_view()),
    path('get_email_phone/', GetEmailAndPhoneApiView.as_view()),
    path('change_password_phone/', ChangePasswordViaPhoneNumber.as_view()),

    # Reset Password URLs
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
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
    path('admin_app/', include("admin_dashboard.urls")),

    # Check Existing Email and Phone Number
    path('check_existing_email/', CheckEmailAPIView.as_view()),
    path('check_existing_phone/', CheckPhoneAPIView.as_view()),

    path('version_control/', VersionControlAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



