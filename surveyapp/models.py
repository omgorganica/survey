import uuid
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    TEXT = 'T'
    SINGLE = 'S'
    MULTIPLE = 'M'

    TYPE_CHOICES = [
        (TEXT, 'Text'),
        (SINGLE, 'One choice'),
        (MULTIPLE, 'Multiple choice'),
    ]
    text = models.CharField(max_length=200, blank=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=2)

    def __str__(self):
        return self.text


class AnswerOption(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_options')

    def __str__(self):
        return self.text


class Survey(models.Model):
    name = models.CharField(max_length=250)
    started = models.DateField(auto_now_add=True)
    finished = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.CharField(max_length=50, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE, related_name='answers')
    user_answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.survey}|{self.question}|{self.user_answer}"
