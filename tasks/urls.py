from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import BoardListCreateAPIView, ColumnListCreateAPIView, TaskListCreateAPIView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('board', BoardListCreateAPIView.as_view()),
    path('column', ColumnListCreateAPIView.as_view()),
    path('task', TaskListCreateAPIView.as_view())

]