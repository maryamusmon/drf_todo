from django.urls import path

from users.views import UserCreateView, UserDetail

urlpatterns = [
    path('/register/', UserCreateView.as_view()),
    path('/', UserDetail.as_view())

]