from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class PaginaPrincipal(TemplateView):
    template_name = 'home/index.html'


class PaginaResultado(TemplateView):
    template_name = 'home/result.html'
