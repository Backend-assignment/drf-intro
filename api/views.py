
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Todo

class TodoView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        data = {
            "results": []
        }
        for todo in todos:
            data["results"].append({
                "task": todo.task,
                "description": todo.description,
                "completed": todo.completed,
                "created_at": todo.created_at,
                "updated_at": todo.updated_at
            })

        return Response(data, status=status.HTTP_200_OK)