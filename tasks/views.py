from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from tasks.models import Tasks, Board
from tasks.serializer import TasksModelSerializer, BoardModelSerializer


class TasksModelViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksModelSerializer


class BoardListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Tasks.objects.all()
        serializer = BoardModelSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     task = Board.objects.get(pk)
    #     serializer = BoardModelSerializer(task, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


