from django import forms 
from ftplib import MAXLINE
from .models import Profesor, Justificacion, Directivos, Administrador
from django.core.exceptions import ValidationError

class IngresarNuevoProfesor(forms.Form):
    class Meta:
        model = Profesor
        fields = ['Nombre', 'Apellidos', 'Matricula', 'Contrasena']


class DirectivoLoginForm(forms.Form):
    Matricula = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput())    


class JustificacionForm(forms.ModelForm):
    class Meta:
        model = Justificacion
        fields = ['motivo']




class DirectivoForm(forms.ModelForm):
    class Meta:
        model = Directivos
        fields = ['Nombre', 'Apellidos', 'Matricula', 'Correo', 'Contrasena']
    
    def clean_Matricula(self):
        matricula = self.cleaned_data.get('Matricula')

        # Verificar en Directivos
        if Directivos.objects.filter(Matricula=matricula).exists():
            raise ValidationError("Esta matrícula ya está registrada en Directivos.")

        # Verificar en Administrador
        if Administrador.objects.filter(Matricula=matricula).exists():
            raise ValidationError("Esta matrícula ya está registrada en Administrador.")

        # Verificar en Profesor
        if Profesor.objects.filter(Matricula=matricula).exists():
            raise ValidationError("Esta matrícula ya está registrada en Profesor.")

        return matricula    


