from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TasksModelViewSet, BoardListAPIView

router = DefaultRouter(trailing_slash=False)
router.register('tasks', TasksModelViewSet, 'task')

urlpatterns = [
    path('', include(router.urls)),
    path('board_task', BoardListAPIView.as_view()),

]