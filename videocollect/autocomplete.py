from dal import autocomplete

from videocollect.models import Signo


class SignoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Signo.objects.all()

        if self.q:
            qs = qs.filter(nombre__contains=self.q)
        else:
            qs = qs[:10]

        return qs