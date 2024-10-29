from django.db import models
from django.utils import timezone

class Administrador (models.Model):
    nombre = models.CharField(max_length=50)
    Matricula = models.CharField(max_length=200)
    Contrasena = models.CharField(max_length=200)

class Directivos(models.Model):
    idDirectivos = models.BigAutoField(primary_key=True, auto_created=True, serialize=False)
    Nombre = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    Matricula = models.CharField(max_length=200)
    Correo = models.CharField(max_length=150)
    Contrasena = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"


class Profesor(models.Model):
    idProfesor = models.BigAutoField(primary_key=True, auto_created=True, serialize=False)
    Nombre = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    Contrasena = models.CharField(max_length=200)
    Matricula = models.CharField(max_length=200)
    Correo = models.CharField(max_length=150)
    idDirectivos = models.ForeignKey(Directivos, on_delete=models.CASCADE)
    imagen_rostro = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"

class PeriodoEscolar(models.Model):
    idPeriodo = models.BigAutoField(primary_key=True, serialize=False)
    Nombre = models.CharField(max_length=60)
    FechaInicio = models.DateTimeField()
    FechaFin = models.DateTimeField()
    
class Horario(models.Model):
    idHorario = models.BigAutoField(primary_key=True, auto_created=True, serialize=False)
    Lunes = models.TimeField(null=True, blank=True)
    Martes = models.TimeField(null=True, blank=True)
    Miercoles = models.TimeField(null=True, blank=True)
    Jueves = models.TimeField(null=True, blank=True)
    Viernes = models.TimeField(null=True, blank=True)
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    idPeriodo =  models.ForeignKey(PeriodoEscolar, on_delete=models.CASCADE) 

    
class DiaAsistencia(models.Model):
    fecha_y_hora = models.DateTimeField(default=timezone.now)
    Tipo = models.CharField(max_length=45)
    idHorario =  models.ForeignKey(Horario, on_delete=models.CASCADE)
    

class Justificacion(models.Model):
    idJustificacion = models.BigAutoField(primary_key=True, auto_created=True, serialize=False)
    motivo = models.CharField(max_length=300)
    estado =  models.CharField(max_length=50)
    idDiaAsistencia =  models.ForeignKey(DiaAsistencia, on_delete=models.CASCADE)
    

class PDFhorario(models.Model):
    idPDFhorario = models.BigAutoField(primary_key=True, auto_created=True, serialize=False)
    FechaModificacion = models.DateTimeField()
    Nombre = models.CharField(max_length=300)
    horario_pdf = models.CharField(max_length=255, null=True, blank=True)
    idHorario =  models.ForeignKey(Horario, on_delete=models.CASCADE)
    

    