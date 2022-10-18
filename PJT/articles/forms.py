from django.forms import ModelForm
from .models import Routines, Routine_result, Routine_day


class RoutineForm(ModelForm):
    class Meta:
        model = Routines
        fields = ("title", "category", "goal")


class Routine_resultForm(ModelForm):
    class Meta:
        model = Routine_result
        fields = "result"


class Routine_dayForm(ModelForm):
    class Meta:
        model = Routine_day
        fields = "day"
