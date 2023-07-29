from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'create_task.html')

def delete_task(request, pk):
    # Get the task by primary key
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        # Handle the task deletion here
        task.delete()
        return redirect('task_list')

    return render(request, 'delete_task.html', {'task': task})

# Define views for updating and deleting tasks similarly.
