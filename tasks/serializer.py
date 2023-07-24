from rest_framework.serializers import Serializer, ModelSerializer

from tasks.models import Tasks, Board


class TasksModelSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class BoardModelSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
