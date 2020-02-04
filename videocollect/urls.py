from django.contrib import admin
from django.urls import path

from videocollect.autocomplete import SignoAutocomplete
from videocollect.views import WelcomeTemplateView, VideoEntrenamientoCreateView

urlpatterns = [
    path('', WelcomeTemplateView.as_view()),
    path('videoupload/', VideoEntrenamientoCreateView.as_view(), name='video_upload'),
    # Autocompletes
    path(
        'signo-autocomplete/$',
        SignoAutocomplete.as_view(),
        name='signo-autocomplete',
    ),
]
