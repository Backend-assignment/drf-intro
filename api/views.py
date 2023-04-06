
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
class TodoView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        print(type(todos[0]))
      
        
        serilazer = TodoSerializer(todos, many=True)
        data = {
            "results": serilazer.data
        }
      


        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        data = request.data
        todo = Todo(
            task=data["task"],
            description=data["description"],
            completed=data["completed"]
        )
        todo.save()
        return Response(status=status.HTTP_200_OK)
        