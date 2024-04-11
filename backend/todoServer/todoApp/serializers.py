from rest_framework import serializers
from .models import Users, Task

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

class TaskSerializer(serializers.ModelSerializer):
    taskStat_display = serializers.CharField(source='get_taskStat_display', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'taskName', 'taskDesc', 'taskStat', 'taskStat_display']