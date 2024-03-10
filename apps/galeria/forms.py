from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    # Metadados da classe
    class Meta:
        # qual model sera espelhado
        model = Fotografia
        # eu quero todos os campos exceto o campo de publicada
        # apenas pessoas administradoras podem controlar esse campo
        exclude = ['publicada', ]

        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário'
        }

        # campos existentes dentro do formulario e passar os css
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            # ja exsistem categorias pré existentes
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
