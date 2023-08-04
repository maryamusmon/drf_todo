from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from .models import Board, Tasks, Column, Subtasks
from .serializer import BoardModelSerializer, TaskSerializer, ColumnSerializer, TaskCreateModelSerializer

column_param = openapi.Parameter(
    'columns',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_STRING),
    description='columnlarni kiriting(ixtiyoriy)',
    required=False
)

subtask_param = openapi.Parameter(
    'subtasks',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_STRING),
    description='subtasklarni kiriting(ixtiyoriy)',
    required=False
)

author_param = openapi.Parameter(
    'author',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(type=openapi.TYPE_STRING),
    description='userni kiriting(ixtiyoriy)',
    required=False
)


class BoardListCreateAPIView(generics.ListCreateAPIView, GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer
    parser_classes = FormParser, MultiPartParser

    @swagger_auto_schema(manual_parameters=[column_param])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        board = serializer.save()
        if li := request.data.get('columns'):
            res = [Column(name=i, board=board) for i in li.split(',')]
            Column.objects.bulk_create(res)
        return Response(serializer.data)


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


class ColumnCreateAPIView(generics.CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


class TaskCreateAPIView(CreateAPIView, GenericViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskCreateModelSerializer
    parser_classes = FormParser, MultiPartParser

    @swagger_auto_schema(manual_parameters=[subtask_param, author_param])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        # for i in request.data.get('author'):
        #     if User.objects.filter(email=i).exists():
        #         Tasks.author.create(task=task, user=User.objects.filter(email=i))
        if li := request.data.get('subtasks'):
            res = [Subtasks(name=i, task=task) for i in li.split(',')]
            Subtasks.objects.bulk_create(res)
        return Response(serializer.data)
