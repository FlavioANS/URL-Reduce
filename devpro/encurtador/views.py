from re import I, S
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from devpro.encurtador.models import UrlRedirect


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)
