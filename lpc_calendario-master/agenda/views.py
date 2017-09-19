from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

def agenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = AgendaMain.objects.all()
    '''for a in lista:
        retorno += '</br>Nome da Agenda: {}</br>'.format(a.nome)

    lista1 = AgendaPrivada.objects.all()
    for a in lista1:
        retorno += '</br>Nome da Agenda: {}</br>'.format(a.nome)'''

    lista2 = AgendaInstitucinal.objects.all()
    for a in lista2:
        retorno += '</br>Nome da Agenda: {}</br>'.format(a.nome)

    return HttpResponse(retorno)

def compromisso(request):
    retorno = "<h1>Compromisso</h1>"
    lista = AgendaInstitucinal.objects.all()
    for a in lista:
        retorno += '</br>Nome da Agenda: {}</br>Compromisso {}'.format(a.nome,a.compromisso)
    return HttpResponse(retorno)
# Create your views here.'''
