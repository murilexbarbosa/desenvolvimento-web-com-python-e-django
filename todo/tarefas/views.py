from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria

from .forms import CategoriaForm,TarefaForm
# Create your views here.


def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Categoria adicionada com sucesso!')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})

def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/lista_categoria.html', {'categorias': categorias})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Tarefa adicionada com sucesso!')
        else:
            print(form.errors)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})
