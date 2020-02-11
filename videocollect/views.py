from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from mega import Mega

from video_collect.local_settings import MEGA_ACCOUNT, MEGA_PASS
from videocollect.apps import VideocollectConfig
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

    success_url = './'

    def form_valid(self, form):

        m = VideocollectConfig.mconnect

        f = form.files['video_entrenamiento_file']
        mega_file = m.upload(f)
        link = m.get_upload_link(mega_file)


        self.object = form.save()
        self.object.video_entrenamiento = link
        messages.add_message(self.request, messages.SUCCESS, 'Se ha guardado correctamente tu aporte')
        return super().form_valid(form)
