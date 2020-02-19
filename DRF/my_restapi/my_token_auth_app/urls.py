from .views import HelloView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('', HelloView.as_view()),
    path('token/', views.obtain_auth_token),
]