from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from .models import Board, Tasks, Column
from .serializer import BoardModelSerializer, TaskSerializer, ColumnSerializer


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

class BoardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskList(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        if Column.objects.filter(pk=kwargs.get('pk')).exists():
            queryset = self.filter_queryset(self.get_queryset().filter(status=kwargs.get('pk')))

            page = self.paginate_queryset(queryset)
            if page is not None:  # router.register('task', )

                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response(data={'error': 'Column does not exists'}, status=status.HTTP_400_BAD_REQUEST)


class ColumnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


