from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria, Tarefa

from .forms import CategoriaForm,TarefaForm
# Create your views here.


@login_required
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


@login_required
def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/lista_categoria.html', {'categorias': categorias})


@login_required
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


@login_required
def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id).delete()
    return redirect('core')


@login_required
def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id).delete()
    return redirect('lista_categoria')


@login_required
def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})


@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'tarefas/nova_categoria.html', {'form': form})
