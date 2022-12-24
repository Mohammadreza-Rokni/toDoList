from rest_framework import serializers
from .models import *

class toDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')
        