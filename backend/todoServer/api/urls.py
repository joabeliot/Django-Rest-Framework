from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('apis/',views.apiList),
    path('additem/',views.addItems),
    path('list/',views.taskList),
    path('add/',views.taskAdd),
    path('update/<str:pk>',views.taskUpdate),
    path('delete/<str:pk>',views.taskDelete),
    path('tatone/<str:pk>/',views.TatOne),
]