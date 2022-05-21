from reset_framework import serializers
from .models import Todo



class TodoSimpleSerializer(serializers.ModelSerializer) :
    """
        serializer for Todo List total search
    """    
    class Meta :
        model = Todo
        fields = ('id', 'title', 'complete', 'important')