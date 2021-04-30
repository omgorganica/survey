from django.contrib import admin
from django.urls import path, include
import rest_framework
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('surveyapp.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

urlpatterns += yasg_urls
