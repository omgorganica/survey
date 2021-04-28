from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet,AnswerViewSet


router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='question')
router.register('answers', AnswerViewSet, basename='question')

urlpatterns = router.urls