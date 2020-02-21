from rest_framework.views import Response
from rest_framework import viewsets

from .serializers import TodoItemSerializer
from .models import TodoItem


class TodoItemListView(viewsets.ViewSet):
    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response(request.data)
