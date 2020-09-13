from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
import glob
import os

from . import func

class PaginaPrincipal(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if not os.path.exists('media/'):
            os.makedirs('media', exist_ok=True)
        for file in glob.glob('media/*.mp4'):
            if file:
                os.remove(file)
        return render(self.request, self.template_name)

    def post(self, request):
        link = str(self.request.POST.get('link-youtube'))
        if link:
            func.videoDownload(link)
            return redirect(reverse_lazy('pagina-resultado'))
        return render(request, 'error.html', {'error': 'erro ao baixar, tente novamente'})


class PaginaResultado(TemplateView):
    template_name = 'home/result.html'

    def get_context_data(self, **kwargs):
        context = super(PaginaResultado, self).get_context_data(**kwargs)
        arquivo = None
        for file in glob.glob('media/*.mp4'):
            arquivo = file
        context['videoDownload'] = arquivo
        return context