from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from functools import wraps
from ..forms import  IngresarNuevoProfesor, IngresarNuevoHorario, PeriodoForm, PeriodoEditar
from ..models import Directivos, Profesor, DiaAsistencia, Horario, PeriodoEscolar, Justificacion
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
    form = IngresarNuevoProfesor()
    
    return render(request, 'Directivo/GestionProfesores.html', {'profesores':profesores, 'form' : form})


@user_is_directivo
def crear_profesor(request):
    if request.method == 'POST':
        form = IngresarNuevoProfesor(request.POST)
        if form.is_valid():
            id  = request.session.get('user_id')
            directivo = Directivos.objects.get(idDirectivos=id)
            profesor = form.save(commit=False)
            profesor.idDirectivos = directivo
            profesor.save()

            return redirect('GestionProfesores')

    return redirect('GestionProfesores')


def BorrarProfesor (request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    profesor.delete()
    return redirect('GestionProfesores')


def  EditarProfesor (request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    
    if request.method == 'POST':
        # Obtén los datos del formulario
        profesor.Nombre = request.POST.get('nombre')
        profesor.Apellidos = request.POST.get('apellido')
        profesor.Matricula = request.POST.get('matricula')
        profesor.Correo  = request.POST.get('Correo')
        profesor.Contrasena  = request.POST.get('Contrasena')

        # Guarda los cambios
        profesor.save()
        
        # Redirige a otra página
        return redirect('GestionProfesores')

    # Si es un método GET, muestra el formulario con los datos del profesor
    return redirect('GestionProfesores')


def CerrarSesionDirectivo(request):
    # Eliminar datos específicos de la sesión
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_rol' in request.session:   
        del request.session['user_rol']
    return redirect("Inicio")


def GestionHorarios(request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    horarios = Horario.objects.filter(idProfesor = profesor)
    form = IngresarNuevoHorario()
    
    return render(request, 'Directivo/GestionHorarios.html', {'horarios' : horarios,'form' : form, 'profesor':profesor})

def EliminarHorario(request,id,idPro):
    horario = get_object_or_404(Horario, idHorario=id)
    horario.delete()
    
    return redirect('GestionHorarios', id =  idPro)


def CrearHorario(request,id):
    if request.method == 'POST':
        form = IngresarNuevoHorario(request.POST)
        if form.is_valid():
            profesor =  get_object_or_404(Profesor, idProfesor=id)
            horario = form.save(commit=False)
            horario.idProfesor = profesor
            horario.save()
            return redirect('GestionHorarios',id = id)
        else:
            return redirect('GestionHorarios',id = id)
    return redirect('GestionHorarios',id = id)


def EditarHorario(request, id):
    # Obtener el horario que se va a editar
    horario = get_object_or_404(Horario, idHorario=id)
    idPro =  horario.idProfesor.idProfesor

    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del POST
        form = IngresarNuevoHorario(request.POST, instance=horario)
        
        if form.is_valid():
            # Guardar la instancia actualizada
            form.save()
            return redirect('GestionHorarios',id = idPro)  # Redirigir a la vista de gestión de horarios
    else:
        # Si no es una solicitud POST, se muestra el formulario con los datos existentes
        return redirect('GestionHorarios',id = idPro) 

    # Renderizar la plantilla con el formulario
    return redirect('GestionHorarios',id = idPro)


def GestionPeriodos(request):
    periodos = PeriodoEscolar.objects.all()
    form = PeriodoForm()
    form2 = PeriodoEditar()
    return render(request, 'Directivo/GestionPeriodos.html', {'periodos': periodos, 'form': form, 'form2': form2})


def EliminarPeriodo (request,id):
    # Obtener el periodo que se va a eliminar
    periodo = get_object_or_404(PeriodoEscolar, idPeriodo=id)
    periodo.delete()
    return redirect('GestionPeriodos')


def CrearPeriodo (request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del POST
        form = PeriodoForm(request.POST)
        if  form.is_valid():
            # Guardar la instancia actualizada
            form.save()
            return redirect('GestionPeriodos')
        else:
            return redirect('GestionPeriodos')
    return redirect('GestionPeriodos')



def  EditarPeriodo (request,id):
    # Obtener el periodo que se va a editar
    periodo = get_object_or_404(PeriodoEscolar, idPeriodo=id)
    
    if  request.method == 'POST':
        # Crear una instancia del formulario con los datos del POST
        form = PeriodoForm(request.POST, instance=periodo)
        
        if  form.is_valid():
            # Guardar la instancia actualizada
            form.save()
            return redirect('GestionPeriodos')
    else:
        return redirect('GestionPeriodos')
        
            
def Justificante (request):
    
    id = request.session.get('user_id')
    
    directivo =  Directivos.objects.get(idDirectivos=id)
    profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)
    horarios =  Horario.objects.filter(idProfesor__in = profesores)

    asistencias = DiaAsistencia.objects.filter(idHorario__in = horarios)
    justificantes  = Justificacion.objects.filter(idDiaAsistencia__in=asistencias)
    
    for justificante in justificantes:
        profesor = Profesor.objects.get(idProfesor=justificante.idDiaAsistencia.idHorario.idProfesor.idProfesor)    
        justificante.profesor = profesor.Matricula
    
    return render (request, 'Directivo/Justificantes.html',{'justificantes':justificantes})


    
def AceptarJustificante (request, id):
    
    justificante = get_object_or_404(Justificacion, idJustificacion=id)
    justificante.estado = 'Aprobado'
    justificante.save()
    asistencia = get_object_or_404(DiaAsistencia, id =  justificante.idDiaAsistencia.id)
    asistencia.Tipo = 'Asistencia';
    asistencia.save()
    
    return redirect ('Justificantes')
    

    

def validar_nombre(request):
    nombre = request.GET.get('nombre')
    directivo_id = request.GET.get('id')  # ID del directivo que estamos editando
    print (directivo_id)
    if nombre:
        # Excluir el `directivo_id` solo en `Directivos`
        if directivo_id:
            existe = (
                PeriodoEscolar.objects.filter(Nombre=nombre).exclude(idPeriodo=directivo_id).exists()
            )
        else:
            existe = (
                PeriodoEscolar.objects.filter(Nombre=nombre).exists()
            )
        return JsonResponse({'existe': existe})
    
    # Respuesta si el `correo` no se proporciona
    return JsonResponse({'error': 'Correo no proporcionado'}, status=400)


def validar_fechas(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_final = request.GET.get('fecha_final')

    # Validar que ambas fechas están presentes
    try:
        es_valido = fecha_inicio <= fecha_final
        return JsonResponse({'es_valido': es_valido})
    except ValueError:
            # Si hay un error de formato, retorna que no es válido
        return JsonResponse({'es_valido': False})
    





