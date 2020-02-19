from django.shortcuts import render
from rest_framework.views import APIView, Response

from .serializers import TodoItemSerializer
from .models import TodoItem


class TodoItemListView(APIView):
    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response(request.data)
