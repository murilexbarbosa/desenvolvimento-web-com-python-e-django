from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from todo.tarefas.models import Tarefa


# Create your views here.
def home(request):
    tarefa = Tarefa.objects.all()
    return render(request, 'core/index.html', {'tarefas': tarefa})

