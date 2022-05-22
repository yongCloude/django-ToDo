from tracemalloc import get_object_traceback
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer

# Create your views here.
class TodosAPIView(APIView) :
    """
        Todo total search View
    """        
    def get(self, request) :
        todos = Todo.objects.filter(complete = False)
        serializer = TodoSimpleSerializer(todos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class TodoAPIView(APIView) :
    """
        Todo detail search View
    """    
    def get(self, request, pk) :
        todo = get_object_or_404(Todo, id = pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
        