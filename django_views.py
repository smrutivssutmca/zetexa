# models.py
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    
    def __str__(self):
        return self.name
        
class Task(models.Model):
    
    STATUS_OPTIONS = [
        ['pending', 'Pending'],
        ['completed', 'Completed']
    ]
     title = models.CharField(max_length=128, blank=True, null=True)
     description = models.TextField()
     assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
     status = models.CharField(max_length=128, choices=STATUS_OPTIONS)
     due_date = models.DateTimeField()
     
     
     
# serializers.py
from rest_framework import serializers
from .models import Task, User


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
# views.py

from rest_framework import APIView
from .models import task, User
from .serilizers import TaskSerializers
from rest_framework.response import Response

class TaskView(APIView):
    
    def get(self, request):
        status = request.query.get('status')
        
        if status:
            tasks = Task.objects.filter(status=status)
        else:
            tasks = Task.objects.all()
            
        serializers = TaskSerializers(tasks, many=True)
        
        return Response(serializers.data)
    
    def post(self, request):
        
        data = request.data
        
        try:
            serialzer = TaskSerializers(data=data)
        
            if serialzer.is_valid():
                serialzer.save()
                
            return Response({"msg": "Task Created"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serialzer.errors, status=status.HTTP_400_ERROR)
        
        
        
# urls.py

from django.urls import path
from .views import TaskView

urlpatterns = [
    path("/tasks/", TaskView.as_view(), name='taskview')
    ]



