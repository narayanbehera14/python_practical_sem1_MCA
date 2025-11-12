from django.shortcuts import render
from.model import Task

def task_list_view(request):
    all_tasks = Task.objects.all()

    context = {
        'task':all_tasks,
        'title':'MVT Task List'
    }