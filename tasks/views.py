# from rest_framework import generics
#
# from tasks.models import Board, Column, Tasks
# from tasks.serializer import BoardModelSerializer, ColumnSerializer, TaskSerializer
#
#
# class BoardListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardModelSerializer
#
#
# class ColumnListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Column.objects.all()
#     serializer_class = ColumnSerializer
#
#
# class TaskListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer
#
#

from rest_framework import generics
from .models import Board
from .serializer import BoardModelSerializer

class BoardListCreateView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

class BoardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer
