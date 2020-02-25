import factory

from .models import TodoItem


class TodoItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = TodoItem
