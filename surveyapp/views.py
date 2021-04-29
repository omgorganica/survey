from rest_framework import generics, viewsets
from .models import Question, AnswerOption, Survey, UserAnswer
from .serializers import QuestionSerializer,AnswerOptionsSerializer, UserAnswerSerializer, SurveySerializer
from rest_framework.permissions import IsAdminUser, AllowAny

# Survey
class SurveyCreateView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAdminUser]


class SurveyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAdminUser]

class SurveyListView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAdminUser]

class ActiveSurveyListView(generics.ListAPIView):
    queryset = Survey.objects.all().exclude(finished__isnull=False)
    serializer_class = SurveySerializer
    permission_classes = [AllowAny]
# Question
class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

# AnswerOption
class AnswerOptionCreateView(generics.CreateAPIView):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionsSerializer
    permission_classes = [IsAdminUser]

class AnswerOptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionsSerializer
    permission_classes = [IsAdminUser]

class AnswerOptionListView(generics.ListAPIView):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionsSerializer
    permission_classes = [AllowAny]

# UserAnswer
class UserAnswerOptionCreateView(generics.CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [AllowAny]