from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Question, AnswerOption, Survey, UserAnswer
from rest_framework.exceptions import ValidationError


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
    answer_option = serializers.PrimaryKeyRelatedField(queryset=AnswerOption.objects.all())
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = UserAnswer
        fields = ['user', 'survey', 'question', 'answer_option', 'user_answer']

    def to_representation(self, obj):
        self.fields['answer_option'] = AnswerOptionsSerializer()
        self.fields['question'] = QuestionSerializer()
        self.fields['survey'] = SurveySerializer()
        return super(UserAnswerSerializer, self).to_representation(obj)

