from django.shortcuts import redirect, render
from .models import Routines
from .forms import RoutineForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    routines = Routines.objects.all()
    context = {
        "routines": routines,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        routine_form = RoutineForm(request.POST)
        if routine_form.is_valid():
            account = routine_form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect("articles:index")
    else:
        routine_form = RoutineForm()
    context = {
        "routine_form": routine_form,
    }
    return render(request, "articles/form.html", context=context)


@login_required
def read(request):
    routines = Routines.objects.all()
    context = {
        "routines": routines,
    }
    return render(request, "articles/read.html", context)


def alarm(request, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    routine.is_alarm = not routine.is_alarm
    routine.save()
    return redirect("articles:read")


def delete(request, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    routine.is_deleted = not routine.is_deleted
    routine.save()
    return redirect("articles:read")


def update(request, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    if request.method == "POST":
        routine_form = RoutineForm(request.POST, request.FILES, instance=routine)
        if routine_form.is_valid():
            routine_form.save()
            return redirect("articles:detail", routine.pk)
    else:
        routine_form = RoutineForm(instance=routine)
    context = {
        "routine_form": routine_form,
    }
    return render(request, "articles/form.html", context)
