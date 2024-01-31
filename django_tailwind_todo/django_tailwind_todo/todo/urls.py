from django.urls import path

from django_tailwind_todo.todo.views import index

urlpatterns = (
    path('', index, name='index'),
    path('add_todo/', index, name='add_todo'),
    path('update_todo/<int:pk>/', index, name='update_todo'),
    # path('delete_todo/<int:pk>/', index, name='delete_todo'),
)