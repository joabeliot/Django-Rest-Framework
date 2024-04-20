from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Items, Tasks
from .serializers import ItemsSerializer, TasksSerializer

@api_view(['GET'])
def getData(request):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItems(request):
    serializer = ItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("error")
    return Response(serializer.data)

@api_view(['GET'])
def apiList(request):
    apilist={
        "Tasks":"/list/",
        "Add":"/add/",
        "Update":"/update/<str:pk>",
        "Delete":"/delete/<str:pk>",
        "tatone":"/tatone/<str:pk>",
    }
    return Response(apilist)

@api_view(['GET'])
def taskList(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TatOne(request, pk):
    tasks = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskAdd(request):
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("error")
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(
       instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Tasks.objects.get(id=pk)
    tasks.delete()
    return Response('Item Deleted!!!')