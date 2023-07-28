from django.urls import path

from tasks.views import BoardListCreateAPIView,BoardRetrieveUpdateDestroyAPIView,TaskRetrieveUpdateDestroyAPIView, TaskList, ColumnRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('board', BoardListCreateAPIView.as_view()),
    path('board/<int:pk>', BoardRetrieveUpdateDestroyAPIView.as_view()),
    path('task/<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('column/<int:pk>', ColumnRetrieveUpdateDestroyAPIView.as_view()),
    path('todolist/<int:pk>', TaskList.as_view()),

]