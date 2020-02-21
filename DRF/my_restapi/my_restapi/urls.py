from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todoapi.urls')),
    path('api-token/', include('my_token_auth_app.urls')),
]
