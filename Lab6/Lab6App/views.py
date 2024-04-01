from django.shortcuts import render, HttpResponseRedirect, reverse
from . import models
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ["student_id","firstName","lastName", "gender"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["course_id"]

def SelectCourse(request,student_id):
    if request.method == "POST":

        student = models.Student.objects.get(pk=student_id)

        course_id = request.POST["course"]
        
        course = models.Course.objects.get(pk=course_id)

        student.courses.add(course)

        return HttpResponseRedirect(reverse("details",args=(student_id)))

def students(request):
    if request.method == "POST":

        form = StudentForm(request.POST)

        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("Lab6App:students"))
    student_list = models.Student.objects.all()

    return render(request, "Lab6App/students.html", {"students" : student_list,
                                                     "form" : StudentForm()}
                                                     )
def courses(request):
        
        if request.method == "POST":
            form = CourseForm(request.POST)
            if(form.is_valid):
                form.save()
                return HttpResponseRedirect(reverse("Lab6App:courses"))
        
        course_list = models.Course.objects.all()
        
        return render(request, "Lab6App/courses.html", {"courses" : course_list,
            "form": CourseForm()}
    )

def details(request, student_id):
    if request.method == "POST":

        student = models.Student.objects.get(pk=student_id)

        course_id = request.POST["course"]

        course = models.Course.objects.get(pk=course_id)

        student.courses.add(course)

        return HttpResponseRedirect(reverse("Lab6App:details", args=(student_id,)))
    student = models.Student.objects.get(pk=student_id)

    registered_courses = student.courses.all()

    available_courses = models.Course.objects.exclude(students=student).all()

    return render(request, "Lab6App/details.html",{
        "student": student,
        "reg_courses": registered_courses,
        "avail_courses": available_courses
    })

# Create your views here.
