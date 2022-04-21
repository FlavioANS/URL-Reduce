from ast import Return
from re import I, S
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from devpro.encurtador.models import UrlRedirect


def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    contexto = {
        'reduce': url_redirect, 
        'url_reduzida': url_reduzida, }
    return render(requisicao, 'encurtador/relatorio.html', contexto)


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)
