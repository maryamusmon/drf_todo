from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskModelViewSet, BoardModelViewSet, ColumnListAPIView

router = DefaultRouter(trailing_slash=False)
router.register('task', TaskModelViewSet)
router.register('board', BoardModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('column/', ColumnListAPIView.as_view())
    # path('board/', BoardListCreateView.as_view()),

]