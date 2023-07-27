from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Board, Tasks, Column
from .pagination import  TasksResultsSetPagination
from .serializer import BoardModelSerializer, TaskSerializer, ColumnListModelSerializer


class BoardModelViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer



class TaskModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TasksResultsSetPagination


class ColumnListAPIView(ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnListModelSerializer