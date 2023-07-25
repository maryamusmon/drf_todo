from rest_framework.serializers import  ModelSerializer

from tasks.models import Column, Board, Tasks, Subtasks


class BoardModelSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

    def to_representation(self, instance: Board):
        rep = super().to_representation(instance)
        if instance.column_set.all():
            rep['columns'] = instance.column_set.values('id', 'name', 'board')
            return rep
        return rep


class ColumnModelSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

    def to_representation(self, instance: Column):
        result = super().to_representation(instance)
        if instance.tasks_set.all():
            result['tasks'] = instance.tasks_set.values('id', 'title', 'description', 'status')
            return result
        return result


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

    def to_representation(self, instance: Tasks):
        result = super().to_representation(instance)
        if instance.subtasks_set.all():
            result['subtasks'] = instance.subtasks_set.values('id', 'name', 'is_completed')
            return result
        return result
