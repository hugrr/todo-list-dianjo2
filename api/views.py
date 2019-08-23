from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Todo, TodoSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class TodoView(APIView):
    def get(self, request, todo_id=None):

        #if username is not None:
        #    todo = Todo.objects.filter(username=username)
        #    serializer = TodoSerializer(todo, many=True)
        #    return Response(serializer.data)
        if todo_id is not None:
            todo = get_object_or_404(Todo, id=todo_id)
            serializer = TodoSerializer(todo, many=False)
            return Response(serializer.data)
        else:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id):
        Todo.objects.get(pk=todo_id).delete()
        message = {
            "msg": "deleted"
        }
        return Response(message, status=status.HTTP_200_OK)
