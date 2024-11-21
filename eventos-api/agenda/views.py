from django.shortcuts import render
from django.http.response import HttpResponse

from agenda.models import eventos

# Create your views here.
def index(request):
    return HttpResponse('Olá, mundo')

def exibir_evento(request):
    evento = eventos[0]
    return render(request=request,context={'evento': evento}, template_name='agenda\evento_web.html')
