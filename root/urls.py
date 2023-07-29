from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import STATIC_URL, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL
from root.swagger import swagger_urls
from users.views import UserTokenObtainPairView, UserTokenRefreshView, UserTokenVerifyView
urlpatterns = []
urlpatterns += swagger_urls +[
                   path('admin/', admin.site.urls),
                   path('api/v1/', include('tasks.urls')),
                   path('users/', include('users.urls')),
                   path('token/create/', UserTokenObtainPairView.as_view(), name='token_create'),
                   path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
                   path('token/verify/', UserTokenVerifyView.as_view(), name='token_verify'),

               ] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
