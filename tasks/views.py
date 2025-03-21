from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        
        Task.objects.create(title=title, description=description, priority=priority, status=status)
        return redirect('task_list')
    
    return render(request, 'add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.priority = request.POST['priority']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    
    return render(request, 'edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def filter_tasks(request, priority):
    tasks = Task.objects.filter(priority=priority)
    return render(request, 'task_list.html', {'tasks': tasks})
