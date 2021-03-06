from django import forms
from .models import Categoria, Tarefa


class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Categoria
        exclude = ('user',)


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ('user',)
