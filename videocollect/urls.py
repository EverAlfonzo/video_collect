from django.contrib import admin
from django.urls import path

from videocollect.ajax import get_url_from_signo
from videocollect.autocomplete import SignoAutocomplete
from videocollect.views import WelcomeTemplateView, VideoEntrenamientoCreateView

urlpatterns = [
    path('', WelcomeTemplateView.as_view()),
    path('videoupload/', VideoEntrenamientoCreateView.as_view(), name='video_upload'),
    # Autocompletes
    path(
        'signo-autocomplete/',
        SignoAutocomplete.as_view(),
        name='signo-autocomplete',
    ),

    # Ajax
    path(
        'url_from_signo/',
        get_url_from_signo,
        name='url_from_signo',
    ),
]
