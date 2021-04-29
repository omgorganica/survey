from rest_framework import generics, viewsets
from .models import Question, AnswerOption, Survey, UserAnswer
from .serializers import QuestionSerializer, AnswerOptionsSerializer, UserAnswerSerializer, SurveySerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from ipware import get_client_ip


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

    def perform_create(self, serializer):
        if self.request.user.id:
            serializer.save(user=self.request.user.id)
        else:
            temporary_user_id, _ = get_client_ip(self.request)
            temporary_user_id = str(temporary_user_id).replace('.', '')
            serializer.save(user=temporary_user_id)


class UserAnswerListView(generics.ListAPIView):
    serializer_class = UserAnswerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = UserAnswer.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
