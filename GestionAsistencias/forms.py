from django import forms 
from ftplib import MAXLINE
from .models import Profesor, Justificacion, Directivos, Administrador,Horario
from django.core.exceptions import ValidationError

class IngresarNuevoProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['Nombre', 'Apellidos', 'Matricula', 'Correo', 'Contrasena']
        


class IngresarNuevoHorario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'idPeriodo']
        widgets = {
            'Lunes': forms.TimeInput(attrs={'type': 'time'}),
            'Martes': forms.TimeInput(attrs={'type': 'time'}),
            'Miercoles': forms.TimeInput(attrs={'type': 'time'}),
            'Jueves': forms.TimeInput(attrs={'type': 'time'}),
            'Viernes': forms.TimeInput(attrs={'type': 'time'}),
        }



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


