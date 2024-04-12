# views.py

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Task
from .serializers import TaskSerializer

class UserView(api_view):
    @api_view(['POST'])
    @csrf_exempt
    def user_create(self, request):
        
        pass

    @api_view(['POST'])
    @csrf_exempt
    def user_login(self, request):
        pass

class TaskView(api_view):

    @api_view(['GET'])
    def Get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    @api_view(['POST'])
    def Create(self,request):
        pass

    @api_view(['GET'])
    def Retrieve(self,request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task does not exist'}, status=404)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    @api_view(['PUT'])
    def Update(self,request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task does not exist'}, status=404)
        pass

    @api_view(['DELETE'])
    def Delete(self,request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task does not exist'}, status=404)

        pass

    @api_view(['GET'])
    def Filter(self,request):
        pass