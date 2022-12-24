from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class ListToDo(generics.ListAPIView):               #Read
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):   #Update
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class CreateToDo(generics.CreateAPIView):           #Create
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class DeleteTodo(generics.DestroyAPIView):          #Delete  
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer