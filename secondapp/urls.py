from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
     path('add-student/', views.add_student, name='add_student'),
       path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

]