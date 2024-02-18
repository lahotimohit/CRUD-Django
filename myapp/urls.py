from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.student_tmp, name='student'),
    path('student/create', views.create, name='create'),
    path('student/roll', views.roll, name='roll'),
    path('student/roll1', views.roll1, name='roll1'),
    path('student/roll/update/<int:roll>', views.update, name='update'),
    path('student/roll/show/<int:roll>', views.show, name='show'),
    path('student/roll2', views.roll2, name='roll2'),
    path('student/roll/delete/<int:roll>', views.delete, name='delete')
]
