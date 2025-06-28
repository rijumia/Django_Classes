from django.shortcuts import render, redirect
from taskManagerApp.models import CustomUserModel, TaskModel
from django.contrib.auth import authenticate, login, logout

def homePage(request):
    return render(request,'home.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homePage')
    return render(request,'login.html')

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username = username,
                fullname = fullname,
                email = email,
                img = img,
                bio = bio,
                password = password,
            )
            return redirect('loginPage')
    return render(request,'register.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def addTask(request):
    if request.method == 'POST':
        todoTitle = request.POST.get('todoTitle')
        todoDescription = request.POST.get('todoDescription')
        todoStatus = request.POST.get('todoStatus')
        todoPriority = request.POST.get('todoPriority')
        todoDueDate = request.POST.get('todoDueDate')

        task = TaskModel.objects.create(
            TaskTitle = todoTitle,
            TaskDescription = todoDescription,
            TaskPriority = todoPriority,
            TaskStatus = todoStatus,
            TaskDueDate = todoDueDate,
        )
        return redirect('listTask')
    return render(request, 'add_task.html')

def updateTask(request, id):
    
    taskupdate = TaskModel.objects.get(id=id)
    if request.method == 'POST':
        taskupdate.TaskTitle = request.POST.get('todoTitle')
        taskupdate.TaskDescription = request.POST.get('todoDescription')
        taskupdate.TaskStatus = request.POST.get('todoStatus')
        taskupdate.TaskPriority = request.POST.get('todoPriority')
        taskupdate.TaskDueDate = request.POST.get('todoDueDate')
        taskupdate.save()
        return redirect('listTask')
    return render(request, 'update_task.html', {'taskupdate': taskupdate})

def listTask(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def DeleteTask(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('listTask')
