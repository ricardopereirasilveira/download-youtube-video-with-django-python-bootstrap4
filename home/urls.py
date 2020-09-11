from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.PaginaPrincipal.as_view(), name='pagina-principal'),
    path('', views.PaginaResultado.as_view(), name='pagina-resultado'),
]