from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from agenda.models import eventos

# Create your views here.
def index(request):
    return HttpResponse('Olá, mundo')

def exibir_evento(request):
    evento = eventos[0]
    template = loader.get_template('agenda\templates\exibir_evento.html')
    rendered_template = template.render(context= {evento: evento}, request=request)
    return HttpResponse(rendered_template)