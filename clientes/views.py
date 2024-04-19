from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Clientes

def cadastro_clientes(request):
    if request.method == "GET":
        return render(request, 'cadastro_clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        apelido = request.POST.get('apelido')
        telefone = request.POST.get('telefone')

        clientes = Clientes(
            nome=nome,
            sobrenome=sobrenome,
            apelido=apelido,
            telefone=telefone        
        )

        clientes.save()

        return redirect('/clientes/listar_clientes')

def listar_clientes(request):
    listando_clientes = Clientes.objects.all()
    return render(request, 'listar_clientes.html', {'listando_clientes': listando_clientes})

        
