from django import forms
from .models import Persona

class IngForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombre','apellido','celular','dni','mail')
        widget={
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.TextInput(attrs={'class':'form-control'}),
        }
        
        labels={
            'nombre':'Nombre',
            'apellido': 'Apellido',
            'celular': 'Tel. Cel.',
            'dni': 'DNI',
            'mail': 'Email',
        }