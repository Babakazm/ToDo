from django.urls import path, include
from . import views  # This imports views from the todo app
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', views.add_todo_item, name='add_todo_item'),
    path('update/<int:id>/', views.update_todo_item, name='update_todo_item'),
    path('delete/<int:id>/', views.delete_todo_item, name='delete_todo_item'),
]