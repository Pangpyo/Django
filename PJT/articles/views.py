from django.shortcuts import redirect, render
from .models import Routine_day, Routine_result, Routines
from .forms import Routine_resultForm, RoutineForm, Routine_dayForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        routine_day_form = Routine_dayForm(request.POST)
        if routine_form.is_valid():
            routine = routine_form.save(commit=False)
            routine.user = request.user
            routine.save()
            print(routine.pk)
            routine_result = Routine_result.objects.create(routine=routine)
            routine_result.save()
            routine_day = routine_day_form.save(commit=False)
            routine_day.routine = routine
            routine_day.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        routine_form = RoutineForm()
        routine_day_form = Routine_dayForm()
    context = {
        "routine_form": routine_form,
        "routine_day_form": routine_day_form,
        "message": {
            "msg": "You have successfully created the routine.",
            "status": "ROUTINE_CREATE_OK",
        },
    }
    return render(request, "articles/form.html", context=context)


@login_required
def read(request, account_pk):
    routines = Routines.objects.filter(user_id=account_pk)
    routine_days = Routine_day.objects.all()
    context = {
        "routines": routines,
        "routine_days": routine_days,
    }
    return render(request, "articles/read.html", context)


@login_required
def alarm(request, account_pk, routine_pk):
    print(account_pk, routine_pk)
    routine = Routines.objects.get(pk=routine_pk)
    routine.is_alarm = not routine.is_alarm
    routine.save()
    return redirect("articles:detail", account_pk, routine_pk)


@login_required
def delete(request, account_pk, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    routine.is_deleted = True
    routine.save()
    messages.success(request, "루틴 삭제가 완료되었습니다")
    return redirect("articles:days", account_pk)


@login_required
def update(request, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    routine_day = Routine_day.objects.get(routine_id=routine_pk)
    if request.method == "POST":
        routine_form = RoutineForm(request.POST, request.FILES, instance=routine)
        routine_day_form = Routine_dayForm(
            request.POST, request.FILES, instance=routine_day
        )
        if routine_form.is_valid():
            routine_form.save()
            routine_day_form.save()
            messages.success(request, "글 수정이 완료되었습니다.")
            return redirect("articles:index")
    else:
        routine_form = RoutineForm(instance=routine)
        routine_day_form = Routine_dayForm(instance=routine_day)
    context = {
        "routine_form": routine_form,
        "routine_day_form": routine_day_form,
        "message": {
            "msg": "The routine has been modified.",
            "status": "ROUTINE_UPDATE_OK",
        },
    }
    return render(request, "articles/form.html", context)


from datetime import date
import calendar


@login_required
def days(request, account_pk):
    today = calendar.day_name[date.today().weekday()]
    routine_days = (
        Routine_day.objects.select_related("routine")
        .filter(day__contains=str(today))
        .filter(routine__user_id=account_pk)
    )
    context = {
        "routine_days": routine_days,
        "today": today,
        "message": {
            "msg": "Routine lookup was successful.",
            "status": "ROUTINE_LIST_OK",
        },
    }
    return render(request, "articles/days.html", context)


def detail(request, account_pk, routine_pk):
    routine = Routines.objects.get(pk=routine_pk)
    routine_day = Routine_day.objects.get(routine_id=routine_pk)
    routine_result = Routine_result.objects.get(routine_id=routine_pk)
    context = {
        "routine": routine,
        "routine_day": routine_day,
        "routine_result": routine_result,
    }
    return render(request, "articles/detail.html", context)


def result(request, account_pk, routine_pk):
    routine_result = Routine_result.objects.get(routine_id=routine_pk)
    if request.method == "POST":
        routine_resultform = Routine_resultForm(
            request.POST, request.FILES, instance=routine_result
        )
        if routine_resultform.is_valid():
            routine_resultform.save()
            messages.success(request, "결과 수정이 완료되었습니다")
            return redirect("articles:detail", account_pk, routine_pk)
    else:
        routine_resultform = Routine_resultForm(instance=routine_result)
    context = {
        "routine_resultform": routine_resultform,
    }
    return render(request, "articles/result.html", context)
