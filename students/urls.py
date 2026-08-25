from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:id>', views.edit_student, name='edit'),
    path('delete/<int:id>', views.delete_student, name='delete'),
]
