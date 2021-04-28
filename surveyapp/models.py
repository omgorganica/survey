import uuid
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=200, blank=False)
    multiple = models.BooleanField(default=False,blank=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text


class QuestionsSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserSurvey(models.Model):
    survey_id = models.UUIDField(default=uuid.uuid4, editable=False)
    started_at = models.DateField(auto_now_add=True)
