from django.contrib import admin

from .models import Question,QuestionsSet,UserSurvey,Answer

admin.site.register(Question)
admin.site.register(QuestionsSet)
admin.site.register(UserSurvey)
admin.site.register(Answer)