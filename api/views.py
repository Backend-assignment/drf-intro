
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
        data = {
            "results": []
        }
        serializer = TodoSerializer(todos[0])
        
        for todo in todos:
            data["results"].append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)