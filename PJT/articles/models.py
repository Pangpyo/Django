from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

# Create your models here.


class Routines(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    MIRACLE = "miracle"
    HOMEWORK = "homework"
    category = models.CharField(
        max_length=9,
        choices=(
            (MIRACLE, "miracle"),
            (HOMEWORK, "homework"),
        ),
        default=MIRACLE,
    )
    goal = models.TextField()
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Routine_result(models.Model):
    routine_id = models.ForeignKey(Routines, on_delete=models.CASCADE)
    NOT = "not"
    TRY = "try"
    DONE = "done"
    PROGRESS = (
        (NOT, "안함"),
        (TRY, "시도"),
        (DONE, "완료"),
    )
    result = models.CharField(choices=PROGRESS, default=NOT, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Routine_day(models.Model):
    MON = "mon"
    TUE = "tue"
    WED = "wed"
    THU = "thu"
    FRI = "fri"
    SAT = "sat"
    SUN = "sun"
    DAY_WEEK = (
        (MON, "월요일"),
        (TUE, "화요일"),
        (WED, "수요일"),
        (THU, "목요일"),
        (FRI, "금요일"),
        (SAT, "토요일"),
        (SUN, "일요일"),
    )
    day = MultiSelectField(
        choices=DAY_WEEK,
        min_choices=1,
        max_choices=7,
    )
    routine_id = models.ForeignKey(Routines, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
