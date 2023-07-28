"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
