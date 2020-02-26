from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APISimpleTestCase, APITransactionTestCase
from .factories import TodoItemFactory
from .views import TodoItemListView
from .models import TodoItem


class TestCaseForTodoItemSimple(APISimpleTestCase):
    #  setUp
    def setUp(self):
        self.todo_item = TodoItemFactory.build(title="Test", done=True)

    #  SimpleTestCase
    def test_create_todo_item_request_factory(self):
        self.assertEqual(self.todo_item.title, "Test")


#  APITestCase
class TestCaseForTodoItem(APITestCase):
    #  setUpTestData
    @classmethod
    def setUpTestData(cls):
        cls.todo_item = TodoItemFactory(title="Test", done=True)

    #  RequestFactory
    def test_get_todo_item_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.get("/todo/api/todo")
        todo_item_view = TodoItemListView.as_view()
        response = todo_item_view(request).render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], self.todo_item.id)

    #  APIClient
    def test_get_todo_item_api_client(self):
        response = self.client.get("/todo/api/todo")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCaseForTodoItemWithTransaction(APITransactionTestCase):
    #  setUpClass
    @classmethod
    def setUpClass(cls):
        TodoItemFactory(title="Test", done=False)

    #  TransactionalTestCase
    def test_transactional_case_for_todo_item(self):
        todo_item = TodoItem.objects.first()
        todo_item.set_done_to_true()
        self.assertEqual(todo_item.title, "Done")
