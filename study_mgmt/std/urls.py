from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/", home),
    path("create_student/", createStudent),
    path("delete-student/<int:roll>", deleteStudent),
    path("edit-student/<int:roll>", updateStudent),
    path("do-edit-student/<int:roll>", doUpdateStudent)
]