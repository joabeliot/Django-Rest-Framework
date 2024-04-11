# views.py

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Task
from .serializers import TaskSerializer

# User views

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def user_create(request):
    pass

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def user_login(request):
    pass

# Task views

@api_view(['GET'])
def taskGist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def taskCreate(request):
    pass

@api_view(['GET'])
def taskRetrieve(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task does not exist'}, status=404)
    serializer = TaskSerializer(task)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task does not exist'}, status=404)
    pass

@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task does not exist'}, status=404)

    pass

@api_view(['GET'])
def taskFilter(request):
    pass
