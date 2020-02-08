from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Redcup(models.Model):
    name = models.CharField(max_length=100)
    rules = models.TextField(max_length=2000, default="Put your rules here!")
    players = models.IntegerField(default=1)
    link = models.URLField(
        max_length=200, default="https://www.youtube.com/watch?v=MpnTP5V5IfE"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"redcup_id": self.id})


class Comment(models.Model):
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.CharField(max_length=1000, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    redcup = models.ForeignKey(Redcup, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-created_date"]

