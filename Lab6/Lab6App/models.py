from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=5,primary_key = True)
    def __str__(self):
        return self.course_id
    
class Student(models.Model):
    student_id = models.CharField(max_length=9, primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    # the gender can be either M or F
    gender = models.CharField(max_length=1)
    courses = models.ManyToManyField(Course, blank=True, related_name="students")

    def __str__(self):
        return f"{self.firstName} {self.lastName}: {self.student_id}"


# Create your models here.
