from django.shortcuts import render
from .models import correspondencia,residencia
from django.http import HttpResponse,JsonResponse
from django.db.models import Q

def index(request):
    Correspondencia= correspondencia.objects.all()

    return render(request, 'Primera.html',{
        'Correspondencia' : Correspondencia
    })


def filtro(request): 
    busqueda= request.GET.get("buscar")
    Residencia=residencia.objects.all()

    if busqueda:
            Residencia= residencia.objects.filters(
                Q(numero_res = busqueda)         
            ).distinct()

    return render(request, 'Primera.html',{'Busqueda':Residencia})