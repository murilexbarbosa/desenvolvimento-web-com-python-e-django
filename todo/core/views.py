from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from todo.tarefas.models import Tarefa


# Create your views here.
@login_required
def home(request):
    tarefa = Tarefa.objects.filter(user=request.user)
    return render(request, 'core/index.html', {'tarefas': tarefa})

