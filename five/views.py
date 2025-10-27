from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
import datetime


def parse_due(v):
    if not v:
        return None
    try:
        return datetime.datetime.strptime(v.strip(), "%Y-%m-%d %H:%M")
    except:
        return None


def task_list(r):
    q = Task.objects.all()
    return render(r, "five/task_list.html", {"tasks": q})


def task_create(r):
    if r.method == "POST":
        a = r.POST.get("title")
        b = r.POST.get("notes", "")
        c = r.POST.get("due", "")
        d = parse_due(c)
        Task.objects.create(title=a, notes=b, due=d)
        return redirect("task_list")
    else:
        return render(r, "five/task_form.html")


def task_update(r, pk):
    t = get_object_or_404(Task, pk=pk)
    if r.method == "POST":
        t.title = r.POST.get("title")
        t.notes = r.POST.get("notes", "")
        u = r.POST.get("due", "")
        t.due = parse_due(u)
        t.save()
        return redirect("task_list")
    else:
        return render(r, "five/task_form.html", {"task": t})


def task_delete(r, pk):
    s = get_object_or_404(Task, pk=pk)
    s.delete()
    return redirect("task_list")


def task_toggle_complete(r, pk):
    v = get_object_or_404(Task, pk=pk)
    if v.is_completed == True:
        v.is_completed = False
    else:
        v.is_completed = True
    v.save()
    return redirect("task_list")
