from django import forms 
from ftplib import MAXLINE
from .models import Profesor, Justificacion, Directivos, Administrador,Horario,PeriodoEscolar, PDFhorario
from django.core.exceptions import ValidationError




class PeriodoForm(forms.ModelForm):
    class Meta:
        model = PeriodoEscolar
        fields = ['Nombre', 'FechaInicio', 'FechaFin']
        widgets = {
            'Nombre': forms.TextInput(attrs={
                'list': 'estaciones',  # Conecta el campo a la lista de opciones
                'placeholder': 'Ejemplo: Verano 2024'
            }),
            'FechaInicio': forms.DateInput(attrs={'type': 'date'}),
            'FechaFin': forms.DateInput(attrs={'type': 'date'}),
        }

class PeriodoEditar(forms.ModelForm):
    class Meta:
        model = PeriodoEscolar
        fields = ['Nombre', 'FechaInicio', 'FechaFin']
        widgets = {
            'Nombre': forms.TextInput(attrs={
                'id': 'id_nombre',  # Asigna un id al campo 'Nombre'
                'list': 'estaciones',
                'placeholder': 'Ejemplo: Verano 2024'
            }),
            'FechaInicio': forms.DateInput(attrs={
                'id': 'id_fecha_inicio',  # Asigna un id al campo 'FechaInicio'
                'type': 'date'
            }),
            'FechaFin': forms.DateInput(attrs={
                'id': 'id_fecha_fin',  # Asigna un id al campo 'FechaFin'
                'type': 'date'
            }),
        }


        

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
            'idPeriodo': forms.Select(attrs={'id':'id_idPeriodo'}),
        }



class EdicionHorario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'idPeriodo']
        widgets = {
            'Lunes': forms.TimeInput(attrs={'type': 'time', 'id': 'lunes_id'}),
            'Martes': forms.TimeInput(attrs={'type': 'time', 'id': 'martes_id'}),
            'Miercoles': forms.TimeInput(attrs={'type': 'time', 'id': 'miercoles_id'}),
            'Jueves': forms.TimeInput(attrs={'type': 'time', 'id': 'jueves_id'}),
            'Viernes': forms.TimeInput(attrs={'type': 'time', 'id': 'viernes_id'}),
            'idPeriodo': forms.Select(attrs={'id': 'id_periodo_id'}),  # Si 'idPeriodo' es un campo de selección
        }
       
class IngresarnuevoPDF(forms.ModelForm):
    class Meta:
        model = PDFhorario
        fields = ['Nombre','horario_pdf','idHorario']


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
    
    


