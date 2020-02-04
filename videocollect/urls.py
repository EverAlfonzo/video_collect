from django.contrib import admin
from django.urls import path

from videocollect.views import WelcomeTemplateView

urlpatterns = [
    path('', WelcomeTemplateView.as_view()),
]
