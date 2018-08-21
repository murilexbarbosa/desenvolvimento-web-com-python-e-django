from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Tarefa

from .forms import CategoriaForm,TarefaForm
# Create your views here.


def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categoria')
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
            return redirect('core')
        else:
            print(form.errors)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})


def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id).delete()
    return redirect('core')


def edita_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST)

