from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from tasks.models import Column, Tasks, Board, Subtasks, AuthorTask
from users.models import User


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtasks
        fields = ('id', 'name', 'is_completed')


class AuthorTaskModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorTask
        fields = '__all__'


class UserTasksModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'image')


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'difficulty', 'subtasks')

    def get_tasks(self, column):
        tasks = Tasks.objects.filter(status=column.id)
        return TaskSerializer(tasks, many=True).data

    def to_representation(self, instance: Tasks):
        rep = super().to_representation(instance)
        rep['author'] = instance.authortask_set.values('author__username', 'author__email')
        return rep


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

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'difficulty', 'subtasks')

    def to_representation(self, instance: Tasks):
        rep = super().to_representation(instance)
        rep['author'] = instance.authortask_set.values('author__username', 'author__email')
        return rep
