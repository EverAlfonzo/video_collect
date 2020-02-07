from django.contrib import messages
from django.http import JsonResponse

from videocollect.models import Signo


def get_url_from_signo(request):
    id_signo = request.GET.get('id_signo', None)

    try:
        signo = Signo.objects.get(id=id_signo)
        url = signo.video
        data = {'url': url}
        return JsonResponse(data)
    except:
        messages.error(request, 'Error durante la obtencion de la url de la seña')
        return JsonResponse({'url':''})