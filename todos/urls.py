from django.urls import path
from . import views

urlpatterns = [
    # Add task
    path('addTask/', views.addTask, name='addTask'),

    # Mark as done
    path('marks_as_done/<int:pk>/', views.marks_as_done, name='marks_as_done'),

    # Mark as uncheck
    path('uncheck/<int:pk>/', views.uncheck, name='uncheck'),

    # Edit task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

]