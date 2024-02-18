from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.student_tmp, name='student'),
    path('student/create', views.create, name='create')
]
