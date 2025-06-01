from django.shortcuts import render, redirect
from studentApp.models import*

def homePage(request):
    return render(request, 'home.html')

def studentPage(request):
    
    if request.method=='POST':
        student = studentModel(
            Student_Name = request.POST.get("student_name"),
            Student_Department = request.POST.get("student_department"),
            Student_City = request.POST.get("student_city"),
            Student_Age = request.POST.get("student_age"),
        )
        student.save()
        return redirect('studentListPage')
    
    return render(request, 'student.html')

def studentListPage(request):
    context = {
        'data' : studentModel.objects.all()
    }
    return render(request, 'studentList.html', context)


def teacherPage(request):
    if request.method=='POST':
        teacher = teacherModel(
            Teacher_Name=request.POST.get("teacher_name"),
            Teacher_Subject=request.POST.get("teacher_subject"),
            Teacher_email=request.POST.get("teacher_email"),
            Teacher_phone=request.POST.get("teacher_phone"),
            Teacher_department=request.POST.get("teacher_department"),
        )
        teacher.save()
        return redirect('teacherListPage')
    return render(request, 'addTeacher.html')

def teacherListPage(request):
    context = {
        'teachers' : teacherModel.objects.all()
    }
    return render(request, 'teacherList.html', context)

def coursePage(request):
    if request.method=='POST':
        course = courseModel(
            Course_Name=request.POST.get("course_name"),
            Course_Code=request.POST.get("course_code"),
            Course_Instructor=request.POST.get("instructor"),
            Course_Credits=request.POST.get("credits"),
            Course_Description=request.POST.get("description"),
        )
        course.save()
        return redirect('courseListPage')
    return render(request, 'course.html')

def courseListPage(request):
    context={
        'courses' : courseModel.objects.all()
    }
    return render(request, 'courseList.html',context)