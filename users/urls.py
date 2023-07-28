from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserTokenObtainPairView, UserTokenRefreshView, UserTokenVerifyView, RegisterUserCreateAPIView, \
    ActivationUserGenericAPIView, PasswordResetGenericAPIView, PasswordResetConfirmUpdateAPIView, UserListAPIView

urlpatterns = [
    path('ragister/', RegisterUserCreateAPIView.as_view(), name='register'),
    path('activate-user/', ActivationUserGenericAPIView.as_view(), name='activated_account'),
    path('reset-password/', PasswordResetGenericAPIView.as_view(), name='reset_password'),
    path('reset-password-confirm/', PasswordResetConfirmUpdateAPIView.as_view(), name='reset_password_confirm'),
    path('user_list', UserListAPIView.as_view(), name='user_list')

]
