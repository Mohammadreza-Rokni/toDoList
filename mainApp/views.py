from rest_framework import generics
from .serializers import toDoSerializer
from .models import toDo
from django.views import generic


class ListCreateToDo(generics.ListCreateAPIView):               #Read & Create
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class UpdateDeleteToDo(generics.RetrieveUpdateDestroyAPIView):   #Update & Delete
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer



#for django template
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return toDo.objects.order_by('-created_at')
    