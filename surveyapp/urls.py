from django.urls import path
from .views import SurveyCreateView, SurveyRetrieveUpdateDestroyView, SurveyListView, QuestionCreateView, \
    QuestionRetrieveUpdateDestroyView, QuestionListView,AnswerOptionCreateView,AnswerOptionRetrieveUpdateDestroyView, \
    AnswerOptionListView, ActiveSurveyListView, UserAnswerOptionCreateView,UserAnswerListView

urlpatterns = [
    # Survey
    path('survey_create', SurveyCreateView.as_view(), name='survey_create'),
    path('survey/<int:pk>/', SurveyRetrieveUpdateDestroyView.as_view(), name='survey'),
    path('survey_list', SurveyListView.as_view(), name='survey_list'),
    path('active_survey_list', ActiveSurveyListView.as_view(), name='active_survey_list'),
    # Question
    path('question_create', QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/', QuestionRetrieveUpdateDestroyView.as_view(), name='question'),
    path('question_list', QuestionListView.as_view(), name='question_list'),
    # AnswerOption
    path('answer_create', AnswerOptionCreateView.as_view(), name='answer_create'),
    path('answer/<int:pk>/', AnswerOptionRetrieveUpdateDestroyView.as_view(), name='answer'),
    path('answer_list', AnswerOptionListView.as_view(), name='answer_list'),
    # UserAnswers
    path('user_answer_create', UserAnswerOptionCreateView.as_view(), name='user_answer_create'),
    # ?user=param for exact user queryset
    path('user_answer_list', UserAnswerListView.as_view(), name='user_answer_list'),
]
