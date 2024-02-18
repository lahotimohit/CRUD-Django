from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.student_tmp, name='student'),
    path('student/create', views.create, name='create'),
    path('student/roll', views.roll, name='roll'),
    path('student/roll/update/<int:roll>', views.update, name='update')
]
