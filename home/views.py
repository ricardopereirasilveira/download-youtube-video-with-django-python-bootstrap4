from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from . import func

class PaginaPrincipal(TemplateView):
    template_name = 'home/index.html'

    def post(self, request):
        link = str(self.request.POST.get('link-youtube'))
        if link:
            func.videoDownload(link)
            return redirect(reverse_lazy('pagina-resultado'))
        return render(request, 'error.html', {'error': 'erro ao baixar, tente novamente'})


class PaginaResultado(TemplateView):
    template_name = 'home/result.html'
