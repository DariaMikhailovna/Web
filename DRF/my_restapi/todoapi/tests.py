from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APISimpleTestCase, APITransactionTestCase
from .factories import TodoItemFactory
from .views import TodoItemListView
from .models import TodoItem


class TestCaseForTodoItemSimple(APISimpleTestCase):
    def test_create_city_request_factory(self):
        todo_item = TodoItemFactory.build(title="Test", done=True)
        self.assertEqual(todo_item.title, "Test")


class TestCaseForTodoItem(APITestCase):

    def test_get_todo_item_request_factory(self):
        todo_item = TodoItemFactory(title="Test", done=True)
        request_factory = APIRequestFactory()
        request = request_factory.get("/todo/api/todo")
        todo_item_view = TodoItemListView.as_view()
        response = todo_item_view(request).render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todo_item_api_client(self):
        todo_item = TodoItemFactory(title="Test", done=True)
        response = self.client.get("/todo/api/todo")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCaseForTodoItemWithTransaction(APITransactionTestCase):
    def test_transactional_case_for_todo_item(self):
        TodoItemFactory(title="Test", done=False)
        todo_item = TodoItem.objects.first()
        todo_item.set_done_to_true()
        self.assertEqual(todo_item.name, "Done")
