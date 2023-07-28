from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import STATIC_URL, STATIC_ROOT
from root.swagger import swagger_urls
from users.views import UserTokenObtainPairView, UserTokenRefreshView, UserTokenVerifyView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('tasks.urls')),
                  path('users/', include('users.urls')),
                  path('token/create/', UserTokenObtainPairView.as_view(), name='token_create'),
                  path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify/', UserTokenVerifyView.as_view(), name='token_verify'),

              ] + swagger_urls + static(STATIC_URL, static_root=STATIC_ROOT)
