from django.contrib import admin
from django.urls import path,include
from Student import views
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('students/<str:slug>/', views.view_student, name='view_student'),
    path('edit/<str:slug>/', views.edit_student, name='edit_student'),
    path('students/<str:slug>/', views.view_student, name='view_student'),
    path('delete/<str:slug>/', views.delete_student, name='delete_student'),
    path('test_db/', views.test_db, name='test_db'),  # New path for testing DB connection
    path('add_city/', views.add_city, name='add_city'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_landrecord/', views.add_landrecord, name='add_landrecord'),
    
]