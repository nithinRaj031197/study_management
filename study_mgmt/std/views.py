from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, "std/home.html", {'students': students})


def createStudent(request):
    if request.method == "POST":
        print("Added")
        # retrieve user inputs
        std_roll = request.POST.get("std_roll")
        std_name = request.POST.get("std_name")
        std_email = request.POST.get("std_email")
        std_address = request.POST.get("std_address")
        std_phone = request.POST.get("std_phone")

        #create an object for models
        s = Student()
        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.address = std_address
        s.phone = std_phone

        s.save()

        return redirect("/std/")

    return render(request, "std/create_student.html", {})


def deleteStudent(request, roll):
    student = Student.objects.get(pk=roll)
    student.delete()

    return redirect("/std/")

def updateStudent(request, roll):
    student = Student.objects.get(pk=roll)
    return render(request, "std/edit_student.html", {'std': student})

def doUpdateStudent(request, roll):
    std_roll = request.POST.get("std_roll")
    std_name = request.POST.get("std_name")
    std_email = request.POST.get("std_email")
    std_address = request.POST.get("std_address")
    std_phone = request.POST.get("std_phone")

    s = Student.objects.get(pk=roll)

    s.roll = std_roll
    s.name = std_name
    s.email = std_email
    s.address = std_address
    s.phone = std_phone

    s.save()
    return redirect("/std/")
