from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def parse_due(value):
    if not value:
        return None
    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d %H:%M")
    except ValueError:
        return None


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "five/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        notes = request.POST.get("notes", "")
        due_text = request.POST.get("due", "")
        due_value = parse_due(due_text)
        Task.objects.create(title=title, notes=notes, due=due_value)
        return redirect("task_list")
    return render(request, "five/task_form.html")


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.notes = request.POST.get("notes", "")
        due_text = request.POST.get("due", "")
        task.due = parse_due(due_text)
        task.save()
        return redirect("task_list")
    return render(request, "five/task_form.html", {"task": task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")


def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_list")
