from datetime import datetime
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from functools import wraps
from ..forms import  IngresarNuevoProfesor, IngresarNuevoHorario, PeriodoForm, PeriodoEditar, EdicionHorario, IngresarnuevoPDF, FormEditdePDF
from ..models import Directivos, Profesor, DiaAsistencia, Horario, PeriodoEscolar, Justificacion, Administrador, PDFhorario
from django.contrib import messages
import os   
from django.conf import settings



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
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    return render(request, "Directivo/InicioDirectivo.html", { 'directivo' : directivo } )


@user_is_directivo
def Reporte(request):
    busqueda = request.GET.get('search', '')
    periodos = PeriodoEscolar.objects.all()
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)
    
    if busqueda:
        try:
            Periodo = PeriodoEscolar.objects.get(Nombre = busqueda)
            horarios = Horario.objects.filter(idPeriodo = Periodo, idProfesor__in = profesores)
            asistencias = DiaAsistencia.objects.filter(idHorario__in = horarios )    
        except PeriodoEscolar.DoesNotExist:
            messages.error(request, 'No se encontraron resultados')
            asistencias = DiaAsistencia.objects.none()
    else:
        horarios = Horario.objects.filter(idProfesor__in = profesores)
        asistencias = DiaAsistencia.objects.filter(idHorario__in = horarios )
    
    for profesor in profesores:
        horarios_pro = horarios.filter(idProfesor=profesor)
        asistencias_pro = asistencias.filter(idHorario__in=horarios_pro)
        profesor.asistencias_count = asistencias_pro.filter(Tipo="Asistencia").count()
        profesor.retardos_count = asistencias_pro.filter(Tipo="Retardo").count()
    
    # Renderizar la plantilla con los datos de profesores
    return render(request, 'Directivo/ReporteDirectivo.html', {'profesores': profesores, 'periodos' : periodos })


@user_is_directivo
def GestionProfesores (request):
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)
    form = IngresarNuevoProfesor()
    
    return render(request, 'Directivo/GestionProfesores.html', {'profesores':profesores, 'form' : form})



def buscar_profesores(request):
    query = request.GET.get('q', '')  # Obtiene el texto de búsqueda
    id = request.session.get('user_id')
    directivo =  Directivos.objects.get(idDirectivos=id)
    if query:
        profesores = Profesor.objects.filter(
            Matricula__icontains=query,
            idDirectivos = directivo.idDirectivos
        )
    else:
        profesores = Profesor.objects.filter(idDirectivos = directivo.idDirectivos)

    data = [
        {
            'id': profesor.idProfesor,
            'nombre': profesor.Nombre,
            'apellidos': profesor.Apellidos,
            'matricula': profesor.Matricula,
            'correo': profesor.Correo,
            'contrasena': profesor.Contrasena
        }
        for profesor in profesores
    ]
    return JsonResponse(data, safe=False)

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

@user_is_directivo
def BorrarProfesor (request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    profesor.delete()
    return redirect('GestionProfesores')

@user_is_directivo
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

def GestionHorariosPDF(request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id) 
    horarios = Horario.objects.filter(idProfesor = profesor)
    horariosPDF = PDFhorario.objects.filter(idHorario__in = horarios)
    form = IngresarnuevoPDF()   
    form2 = EdicionHorario()
    
    return render(request, 'Directivo/GestionHorariosPDF.html', {'horarios' : horarios, 'PDFs' : horariosPDF, 'form' : form, 'profesor':profesor, 'form2' : form2})



def GestionHorarios(request, id):
    profesor = get_object_or_404(Profesor, idProfesor=id)
    horarios = Horario.objects.filter(idProfesor = profesor)
    horariosPDF = PDFhorario.objects.filter(idHorario__in = horarios)
    
    for horario in horarios:
    # Añades un flag para verificar si existe un PDF para cada horario
        horario.has_pdf = any(pdf.idHorario.idHorario == horario.idHorario for pdf in horariosPDF)
    
    form = IngresarNuevoHorario()
    form2 = EdicionHorario()
    form3 = IngresarnuevoPDF()
    form4 = FormEditdePDF()
    
    return render(request, 'Directivo/GestionHorarios.html', {'horarios' : horarios, 'horariosPDF': horariosPDF, 'form' : form, 'profesor':profesor, 'form2' : form2, 'form3' : form3, 'form4': form4})




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



def buscar_periodos(request):
    query = request.GET.get('q', '')  # Obtiene el texto de búsqueda
    if query:
        periodos = PeriodoEscolar.objects.filter(
            Nombre__icontains=query
        )
    else:
        periodos = PeriodoEscolar.objects.all()

    data = [
        {
            'id': periodo.idPeriodo,
            'nombre': periodo.Nombre,
            'fechainicio': periodo.FechaInicio.strftime('%Y-%m-%d'),
            'fechafin': periodo.FechaFin.strftime('%Y-%m-%d')
        }
        for periodo in periodos
    ]
    return JsonResponse(data, safe=False)



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


def crear_pdf(request, id, idHorario):
    if request.method == 'POST':
        form = IngresarnuevoPDF(request.POST, request.FILES)
        if form.is_valid():
            pdf_horario = form.save(commit=False)
            pdf_horario.FechaModificacion = timezone.now()
            horario = Horario.objects.get(idHorario = idHorario)
            pdf_horario.idHorario = horario
            pdf_horario.save()
            return redirect('GestionHorarios', id=id)  # Redirige usando el `idProfesor`
        else:
            # Renderiza de nuevo la página con el formulario y los errores
            return redirect('GestionHorarios', id=id)

    else:
        return redirect('GestionHorarios', id=id)
    
def EliminarPDF(reques, id, idPro):
    PDF = get_object_or_404(PDFhorario, idPDFhorario=id)
    
    if PDF.horario_pdf:
        file_path = os.path.join(settings.MEDIA_ROOT, PDF.horario_pdf.name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            
            
    PDF.delete()
    return redirect('GestionHorarios', id=idPro)

    

def EditarPDF(request, id, idPro):
    pdf = get_object_or_404(PDFhorario, idPDFhorario=id)
    if request.method == 'POST':
        form = IngresarnuevoPDF(request.POST, request.FILES, instance=pdf)
        if form.is_valid():
            # Actualiza la fecha de modificación
            pdf.FechaModificacion = timezone.now()
            pdf = form.save(commit=False)
            pdf.save()  
            return redirect('GestionHorarios', id=idPro)
    return redirect('GestionHorarios', id=idPro)

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
    print ("hola {directivo_id}")
    
    
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
    if fecha_inicio and fecha_final:
        try:
            # Convertir las fechas a objetos datetime
            fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_final_dt = datetime.strptime(fecha_final, '%Y-%m-%d')

            # Comparar las fechas
            es_valido = fecha_inicio_dt <= fecha_final_dt
            return JsonResponse({'es_valido': es_valido})
        except ValueError:
            # Si hay un error de formato, retorna que no es válido
            return JsonResponse({'es_valido': False})
    else:
        # Retorna que no es válido si alguna fecha falta
        return JsonResponse({'es_valido': False})

    
def validar_matricula_profesor(request):
    matricula = request.GET.get('matricula')
    profesor_id = request.GET.get('id')  # ID del directivo que estamos editando
    if matricula:
        # Excluir el `directivo_id` solo en `Directivos`
        if profesor_id:
            existe = (
                Directivos.objects.filter(Matricula=matricula).exists() or
                Administrador.objects.filter(Matricula=matricula).exists() or
                Profesor.objects.filter(Matricula=matricula).exclude(idProfesor=profesor_id).exists()
            )
        else:
            existe = (
                Directivos.objects.filter(Matricula=matricula).exists() or
                Administrador.objects.filter(Matricula=matricula).exists() or
                Profesor.objects.filter(Matricula=matricula).exists()
            )
        return JsonResponse({'existe': existe})
    
    
    


def validar_correo_profesor(request):
    correo = request.GET.get('correo')
    profesor_id = request.GET.get('id')  # ID del directivo que estamos editando
    print (profesor_id)
    if correo:
        # Excluir el `directivo_id` solo en `Directivos`
        if profesor_id:
            existe = (
                Directivos.objects.filter(Correo=correo).exists() or
                Profesor.objects.filter(Correo=correo).exclude(idProfesor=profesor_id).exists()
            )
        else:
            existe = (
                Directivos.objects.filter(Correo=correo).exists() or
                Profesor.objects.filter(Correo=correo).exists()
            )
        return JsonResponse({'existe': existe})
    
    # Respuesta si el `correo` no se proporciona
    return JsonResponse({'error': 'Correo no proporcionado'}, status=400)




def validar_periodo_profesor(request):
    id_periodo = request.GET.get('idPeriodo')
    profesor_id = request.GET.get('profesorId')
    id_horario = request.GET.get('id')
    
    print("hola")
    if id_horario:
        if Horario.objects.filter(idPeriodo=id_periodo, idProfesor=profesor_id).exclude(idHorario =id_horario).exists():
            return JsonResponse({'existe': True})
    else:
        if Horario.objects.filter(idPeriodo=id_periodo, idProfesor=profesor_id).exists():
            return JsonResponse({'existe': True})
    return JsonResponse({'existe': False})




