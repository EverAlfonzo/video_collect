from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from videocollect.forms import VideoEntrenamientoForm


class WelcomeTemplateView(TemplateView):
    template_name = 'Home.html'

    def get(self, request, *args, **kwargs):
        if 'colaborar' in request.GET:
            return redirect('video_upload')
        else:
            return super(WelcomeTemplateView, self).get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        print('hola')


class VideoEntrenamientoCreateView(CreateView):
    form_class = VideoEntrenamientoForm
    template_name = 'video_upload_form.html'
