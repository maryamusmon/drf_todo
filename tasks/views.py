from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Board, Tasks
from .serializer import BoardModelSerializer, TaskSerializer


class BoardListCreateView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

class BoardModelViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer
# class BoardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardModelSerializer
#

class TaskModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

# class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer
