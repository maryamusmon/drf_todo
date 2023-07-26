from rest_framework.relations import RelatedField
from rest_framework.serializers import ModelSerializer

from tasks.models import Column, Board, Tasks


class SubTaskSerializer(RelatedField):

    def to_representation(self, value):
        return {'id': value.id, 'title': value.name}


class TasksSerializer(ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'subtasks')


class BoardModelSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

    def to_representation(self, instance: Board):
        rep = super().to_representation(instance)
        if instance.columns.all():
            result = []
            for column in instance.columns.values('id', 'name', 'board'):
                tasks = []
                for task in instance.columns.values('tasks__id', 'tasks__title', 'tasks__description', 'tasks__status'):
                    if task.get('tasks__status') == column.get('id'):
                        subtasks = []
                        for subtask in instance.columns.values('tasks__subtasks', 'tasks__subtasks__name',
                                                               'tasks__subtasks__is_completed', 'tasks'):
                            if subtask.get('tasks') == task.get('tasks__id'):
                                subtasks.append(subtask)
                            else:
                                continue
                        task['subtasks'] = subtasks
                        tasks.append(task)
                    else:
                        continue
                # column['tasks'] = TasksSerializer(column, many=True, read_only=True)
                column['tasks'] = tasks
                result.append(column)
            rep['columns'] = result
            return rep
        return rep


class ColumnModelSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

    def to_representation(self, instance: Column):
        result = super().to_representation(instance)
        if instance.tasks.all():
            result['tasks'] = instance.tasks_set.values('id', 'title', 'description', 'status')
            return result
        return result


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

    def to_representation(self, instance: Tasks):
        result = super().to_representation(instance)
        if instance.subtasks.all():
            result['subtasks'] = instance.subtasks_set.values('id', 'name', 'is_completed')
            return result
        return result
