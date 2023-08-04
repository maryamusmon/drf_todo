from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from tasks.models import Column, Tasks, Board, Subtasks
from users.models import User


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtasks
        fields = ('id', 'name', 'is_completed')


class UserTasksModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'image')


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)
    author = UserTasksModelSerializer(many=True)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'difficulty', 'subtasks', 'author')

    def get_tasks(self, column):
        tasks = Tasks.objects.filter(status=column.id)
        return TaskSerializer(tasks, many=True).data


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name', 'board')

    def get_tasks(self, column):
        tasks = Tasks.objects.filter(status=column.id)
        return TaskSerializer(tasks, many=True).data

class ColumnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name')

    def get_tasks(self, column):
        tasks = Tasks.objects.filter(status=column.id)
        return TaskSerializer(tasks, many=True).data


class BoardModelSerializer(serializers.ModelSerializer):
    columns = ColumnTaskSerializer(many=True, read_only=True)
    id = IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'columns')


class TaskCreateModelSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    author = UserTasksModelSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'difficulty', 'subtasks', 'author')

