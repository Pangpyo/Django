from django.db import models
from django.conf import settings

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
