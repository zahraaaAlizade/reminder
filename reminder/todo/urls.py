from django.urls import path
from todo.views import *

urlpatterns = [
   
    path('', indexView),
    path('post/ajax/task', PostTask, name = "post_tasks"),
    path('get/ajax/validate/taskname', CheckTask, name = "validate_taskname"),
    path("cbv/", TaskView.as_view(), name = "task"),
    path('', HomeView.as_view(),name="home"),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('categorytask/<int:id>/',categorytasks,name="c_task"),

]