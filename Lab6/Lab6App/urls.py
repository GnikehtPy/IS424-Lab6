from django.urls import path
from . import views

app_name = "Lab6App"

urlpatterns = [
    path("students/", views.students, name="students"),
    path("courses/", views.courses, name="courses"),
    path("details/<str:student_id>", views.details, name="details")
]