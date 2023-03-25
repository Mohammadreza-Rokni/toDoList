from rest_framework import serializers
from .models import toDo

class toDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDo # my model name
        fields = ('id', 'title', 'Description', 'created_at','update_at','isCompleted') # give it the filds we want
        