from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    # return HttpResponse("Home")
    return render(request, 'revenues/home.html', context={
        'nome':'Leonardo',
        'nascimento':'25 de maio de 1971',
        'idade': 54
    })




def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return render(request, 'revenues/contato.html')
