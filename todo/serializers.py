from rest_framework import serializers
from .models import Todo



class TodoSimpleSerializer(serializers.ModelSerializer) :
    """
        serializer for Todo List total search
    """    
    class Meta :
        model = Todo
        fields = ('id', 'title', 'complete', 'important')
        
class TodoDetailSerializer(serializers.ModelSerializer) :
    """
        Serializer for Todo List detail search
    """    
    class Meta :
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')
        
class TodoCreateSerializer(serializers.ModelSerializer) :
    """
        Serializer for Todo List create
    """    
    class Meta : 
        model = Todo
        field = ('title', 'description', 'important')
