from django.urls import path

from .views import TodoItemListView

urlpatterns = [
    path('api/todo', TodoItemListView.as_view())
]
