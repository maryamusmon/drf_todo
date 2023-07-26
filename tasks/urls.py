from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import BoardListCreateView, BoardRetrieveUpdateDestroyView, TasksRetrieveUpdateDestroyAPIView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    # path('', include(router.urls)),
    path('board_list', BoardListCreateView.as_view()),
    path('board', BoardRetrieveUpdateDestroyView.as_view()),
    path('task', TasksRetrieveUpdateDestroyAPIView.as_view())

]