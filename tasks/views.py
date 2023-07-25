from rest_framework import generics

from tasks.models import Board, Column, Tasks
from tasks.serializer import BoardModelSerializer, ColumnModelSerializer, TaskModelSerializer


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer


class ColumnListCreateAPIView(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnModelSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskModelSerializer


