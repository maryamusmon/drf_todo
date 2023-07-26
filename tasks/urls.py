from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import  BoardListCreateView,  BoardRetrieveUpdateDestroyView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('board', BoardListCreateView.as_view()),
    path('board_retrive', BoardRetrieveUpdateDestroyView.as_view())

]