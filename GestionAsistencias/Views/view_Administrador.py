from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from ..models import DiaAsistencia, Directivos, Horario, Profesor, PeriodoEscolar
from functools import wraps
from ..forms import  DirectivoForm


def user_is_administrador(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Obtener el rol del usuario desde la sesión
        rol = request.session.get('user_rol')
        
        # Verificar si el rol es 'Profesor'
        if rol == "Administrador":
            return view_func(request, *args, **kwargs)
        else:
            return render(request,"No_acceso.html")
    
    return _wrapped_view

def CerrarSesionAdmin(request):
    # Eliminar datos específicos de la sesión
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_rol' in request.session:   
        del request.session['user_rol']
    return redirect("Inicio")

def GestionarDirectivo(request):
    directivos = Directivos.objects.all()
    form = DirectivoForm() 
    return render(request, 'Administrador/GestionDirectivos.html', {'directivos': directivos, 'form': form})

def EditarDirectivo(request, id):
    directivo = get_object_or_404(Directivos, idDirectivos=id)
    
    if request.method == 'POST':
        # Actualiza los campos del directivo
        directivo.Nombre = request.POST.get('nombre')
        directivo.Apellidos = request.POST.get('apellido')  
        directivo.Matricula = request.POST.get('matricula')  
        directivo.Contrasena = request.POST.get('Contrasena')  
        directivo.Correo = request.POST.get('Correo')  

        # Guarda los cambios
        directivo.save()
        
        # Redirige a la página de gestión de directivos
        return redirect('GestionarDirectivos')
    
    # Si es un GET o cualquier otro método, redirige a la página de gestión
    return redirect('GestionarDirectivos')


def BorrarDirectivo (request, id):
    directivo = get_object_or_404(Directivos, idDirectivos=id)
    directivo.delete()
    return redirect('GestionarDirectivos')

@user_is_administrador
def InicioAdmnistrador(request):
    return render(request, "Administrador/InicioAdministrador.html")



def crear_directivo(request):
    if request.method == 'POST':
        form = DirectivoForm(request.POST)
        if form.is_valid():
            form.save()  # Crea y guarda el nuevo Directivo en la base de datos
            return redirect('GestionarDirectivos')  # Redirige a la lista de directivos o a otra página
    else:
        form = DirectivoForm()
    
    return render(request, 'Administrador/CrearAdministrador.html', {'form': form})


def ReporteAsis(request):
    # Obtener el parámetro de búsqueda
    busqueda = request.GET.get('search', '')
    
    # Obtener el ID de usuario de la sesión (si es necesario)
    id = request.session.get('user_id')
    
    # Obtener todos los profesores
    profesores = Profesor.objects.all()
    
    # Filtrar asistencias y horarios según la búsqueda
    if busqueda:
        try:
            # Buscar el periodo escolar por nombre
            periodo = PeriodoEscolar.objects.get(Nombre=busqueda)
            # Obtener el horario asociado al periodo
            horarios = Horario.objects.filter(idPeriodo=periodo)
            # Filtrar las asistencias con los horarios y profesores
            asistencias = DiaAsistencia.objects.filter(idProfesor__in=profesores, idHorario__in=horarios)
        except PeriodoEscolar.DoesNotExist:
            messages.error(request, 'No se encontraron resultados')
            asistencias = DiaAsistencia.objects.none()
    else:
        # Si no hay búsqueda, obtener todas las asistencias y horarios
        asistencias = DiaAsistencia.objects.all()
        horarios = Horario.objects.all()

    # Procesar cada profesor para contar asistencias y retardos
    for profesor in profesores:
        # Filtrar horarios del profesor
        horarios_pro = horarios.filter(idProfesor=profesor)
        # Filtrar asistencias del profesor según los horarios
        asistencias_pro = asistencias.filter(idHorario__in=horarios_pro)
        
        # Contar el número de asistencias y retardos
        profesor.asistencias_count = asistencias_pro.filter(Tipo="Asistencia").count()
        profesor.retardos_count = asistencias_pro.filter(Tipo="Retardo").count()

    # Renderizar la plantilla con los datos de profesores
    return render(request, 'Administrador/ReporteAsistencias.html', {'profesores': profesores})
