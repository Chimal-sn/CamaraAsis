from django.shortcuts import get_object_or_404, redirect, render
from functools import wraps
from ..forms import  IngresarNuevoProfesor
from ..models import Directivos, Profesor, DiaAsistencia, Horario, PeriodoEscolar
from django.contrib import messages


def user_is_directivo(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Obtener el rol del usuario desde la sesión
        rol = request.session.get('user_rol')
        
        # Verificar si el rol es 'Profesor'
        if rol == "Directivo":
            return view_func(request, *args, **kwargs)
        else:
            return render(request,"No_acceso.html")
    
    return _wrapped_view

@user_is_directivo
def CasaDirectivo(request):
    return render(request, "Directivo/InicioDirectivo.html")

@user_is_directivo
def crear_profesor(request):
    if request.method == 'POST':
        form = IngresarNuevoProfesor(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['Nombre']
            apellidos = form.cleaned_data['Apellidos'] 
            contrasena = form.cleaned_data['Contrasena']
            iddirectivo = request.session.get('user_id')
            directivo = Directivos.objects.get(idDirectivos=iddirectivo)
            
            nuevo_profesor = Profesor(idDirectivos = directivo, Nombre = nombre, Apellidos = apellidos, Contrasena = contrasena)
            
            nuevo_profesor.save()
            
    else:
        form = IngresarNuevoProfesor()
    
    return render(request, 'Directivo/crear_profesor.html', {'form': form})


def periodo(request):
    busqueda = request.GET.get('search', '')
    
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)
    
    if busqueda:
        try:
            Periodo = PeriodoEscolar.objects.get(Nombre = busqueda)
            horario = Horario.objects.get(idPeriodo = Periodo)
            asistencias = DiaAsistencia.objects.filter(idProfesor__in = profesores, idHorario = horario )    
        except PeriodoEscolar.DoesNotExist:
            messages.error(request, 'No se encontraron resultados')
    else:
        asistencias =  DiaAsistencia.objects.filter(idProfesor__in = profesores)
    
    for profesor in profesores:
        profesor_asistencias = asistencias.filter(idProfesor=profesor)  # Asegura que esto esté correcto
        profesor.asistencias_count = profesor_asistencias.filter(Tipo="Asistencia").count()
        profesor.retardos_count = profesor_asistencias.filter(Tipo="Retardo").count()
    
    # Renderizar la plantilla con los datos de profesores
    return render(request, 'Directivo/VerPeriodo.html', {'profesores': profesores})


@user_is_directivo
def GestionProfesores (request):
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)
    
    return render(request, 'Directivo/GestionProfesores.html', {'profesores':profesores})


def BorrarProfesor (request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    profesor.delete()
    return redirect('GestionProfesores')


def  EditarProfesor (request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    
    if request.method == 'POST':
        # Obtén los datos del formulario
        profesor.Nombre = request.POST.get('nombre')
        profesor.Apellido = request.POST.get('apellido')
        profesor.Matricula = request.POST.get('matricula')
        
        # Guarda los cambios
        profesor.save()
        
        # Redirige a otra página
        return redirect('GestionProfesores')

    # Si es un método GET, muestra el formulario con los datos del profesor
    return render(request, 'Directivo/EditarProfesor.html', {'profesor': profesor})


