from django.forms import CharField, ModelForm
from .models import Routines


class RoutineForm(ModelForm):
    class Meta:
        model = Routines
        fields = ("title", "category", "goal")
