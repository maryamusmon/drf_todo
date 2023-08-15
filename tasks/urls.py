from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import (
    BoardListCreateAPIView,
    BoardRetrieveUpdateDestroyAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    TaskList,
    ColumnRetrieveUpdateDestroyAPIView,
    ColumnCreateAPIView,
    TaskCreateAPIView,
)

# router = DefaultRouter()
# router.register(r'boards', BoardListCreateAPIView, basename='board')
# router.register(r'task', TaskCreateAPIView, basename='task')

board_list = BoardListCreateAPIView.as_view({
    'get': 'list',
    'post': 'create'

})

task_create = TaskCreateAPIView.as_view({
    'post': 'create',
})
urlpatterns = [
    # path('', include(router.urls)),
    path('board/<int:pk>', BoardRetrieveUpdateDestroyAPIView.as_view()),
    path('task/<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('column/create', ColumnCreateAPIView.as_view()),
    path('column/<int:pk>', ColumnRetrieveUpdateDestroyAPIView.as_view()),
    path('task/list/<int:pk>', TaskList.as_view()),
    path('board_list', board_list, name='board'),
    path('task_create', task_create, name='task')
]
