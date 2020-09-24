from dal import autocomplete
from django.db.models import Count

from videocollect.constants import MAX_VIDEOS
from videocollect.models import Signo, VideoEntrenamiento


class SignoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Signo.objects.all()
        videos_entrenamiento = VideoEntrenamiento.objects.values('signo_id')\
            .annotate(video_count=Count("signo_id")).filter(video_count__gte=MAX_VIDEOS).order_by().values_list('signo_id')
        qs = qs.exclude(id__in=videos_entrenamiento)
        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        else:
            qs = qs[:10]

        return qs