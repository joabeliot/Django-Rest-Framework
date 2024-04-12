from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('signin/',views.userCreate, name='UserCreate'),
    path('loginin/',views.userLogin, name='UserLogin'),
    path('taskget/',views.taskGet, name='TaskGet'),
    path('taskcreate/',views.taskCreate, name='TaskCreate'),
    path('taskretrieve/',views.taskRetrieve, name='TaskRetrieve'),
    path('taskupdate/',views.taskUpdate, name='TaskUpdate'),
    path('taskdelete/',views.taskDelete, name='TaskDelete'),
    path('taskfilter/',views.taskFilter, name='TaskFilter'),

    path('api/user/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/user/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]