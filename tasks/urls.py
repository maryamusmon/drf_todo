from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import BoardListCreateView, TaskModelViewSet, BoardModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register('task_crud', TaskModelViewSet)
router.register('board', BoardModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('board_list', BoardListCreateView.as_view()),

]