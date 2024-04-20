from rest_framework import serializers
from base.models import Items, Tasks

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'