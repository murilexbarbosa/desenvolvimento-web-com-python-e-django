from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'nova-categoria/', views.nova_categoria, name='nova_categoria'),
    url(r'nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
]