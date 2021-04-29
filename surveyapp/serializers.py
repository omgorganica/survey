from rest_framework import serializers
from .models import Question, AnswerOption, Survey, UserAnswer
import shortuuid


# shortuuid.uuid()

class AnswerOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
        read_only_fields = ('started',)


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['user','survey','question','answer_option','user_answer']
        extra_kwargs = {'survey': {'required': True}}
        depth = 1
