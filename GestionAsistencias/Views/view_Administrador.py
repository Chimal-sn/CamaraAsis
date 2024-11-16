from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from ..models import DiaAsistencia, Directivos, Horario, Profesor, PeriodoEscolar, Administrador
from functools import wraps
from ..forms import  DirectivoForm
from django.http import JsonResponse

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
    
    return redirect('GestionarDirectivos')



def ReporteAsis(request):
    # Obtener todos los periodos escolares para mostrarlos en el dropdown
    periodos = PeriodoEscolar.objects.all()

    # Obtener el término de búsqueda
    busqueda = request.GET.get('search', '')

    # Lógica existente para procesar la búsqueda
    profesores = Profesor.objects.all()
    if busqueda:
        try:
            periodo = PeriodoEscolar.objects.get(Nombre=busqueda)
            horarios = Horario.objects.filter(idPeriodo=periodo)
            asistencias = DiaAsistencia.objects.filter(idHorario__in=horarios)
        except PeriodoEscolar.DoesNotExist:
            messages.error(request, 'No se encontraron resultados')
            asistencias = DiaAsistencia.objects.none()
    else:
        asistencias = DiaAsistencia.objects.all()
        horarios = Horario.objects.all()

    for profesor in profesores:
        horarios_pro = horarios.filter(idProfesor=profesor)
        asistencias_pro = asistencias.filter(idHorario__in=horarios_pro)
        profesor.asistencias_count = asistencias_pro.filter(Tipo="Asistencia").count()
        profesor.retardos_count = asistencias_pro.filter(Tipo="Retardo").count()

    return render(
        request,
        'Administrador/ReporteAsistencias.html',
        {'profesores': profesores, 'periodos': periodos}
    )
    

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generar_reporte_pdf(request):
    # Obtener los datos necesarios
    busqueda = request.GET.get('search', '')
    profesores = Profesor.objects.all()
    
    if busqueda:
        try:
            periodo = PeriodoEscolar.objects.get(Nombre=busqueda)
            horarios = Horario.objects.filter(idPeriodo=periodo)
            asistencias = DiaAsistencia.objects.filter(idHorario__in=horarios)
        except PeriodoEscolar.DoesNotExist:
            asistencias = DiaAsistencia.objects.none()
    else:
        asistencias = DiaAsistencia.objects.all()
        horarios = Horario.objects.all()

    for profesor in profesores:
        horarios_pro = horarios.filter(idProfesor=profesor)
        asistencias_pro = asistencias.filter(idHorario__in=horarios_pro)
        profesor.asistencias_count = asistencias_pro.filter(Tipo="Asistencia").count()
        profesor.retardos_count = asistencias_pro.filter(Tipo="Retardo").count()

    # Crear el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_asistencias.pdf"'
    
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Título del reporte
    pdf.drawString(200, 750, "Reporte de Asistencias")
    pdf.drawString(100, 730, f"Periodo: {busqueda if busqueda else 'Todos los periodos'}")
    
    # Encabezados de la tabla
    pdf.drawString(50, 700, "Matrícula")
    pdf.drawString(200, 700, "Asistencias")
    pdf.drawString(350, 700, "Retardos")

    # Datos de los profesores
    y = 680  # Altura inicial
    for profesor in profesores:
        pdf.drawString(50, y, str(profesor.Matricula))
        pdf.drawString(200, y, str(profesor.asistencias_count))
        pdf.drawString(350, y, str(profesor.retardos_count))
        y -= 20
        if y < 50:  # Salto de página si hay demasiados datos
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    pdf.save()
    return response



def validar_matricula(request):
    matricula = request.GET.get('matricula')
    directivo_id = request.GET.get('id')  # ID del directivo que estamos editando
    if matricula:
        # Excluir el `directivo_id` solo en `Directivos`
        if directivo_id:
            existe = (
                Directivos.objects.filter(Matricula=matricula).exclude(idDirectivos=directivo_id).exists() or
                Administrador.objects.filter(Matricula=matricula).exists() or
                Profesor.objects.filter(Matricula=matricula).exists()
            )
        else:
            existe = (
                Directivos.objects.filter(Matricula=matricula).exists() or
                Administrador.objects.filter(Matricula=matricula).exists() or
                Profesor.objects.filter(Matricula=matricula).exists()
            )
        return JsonResponse({'existe': existe})
    
    # Respuesta si la `matricula` no se proporciona
    return JsonResponse({'error': 'Matrícula no proporcionada'}, status=400)



def validar_correo(request):
    correo = request.GET.get('correo')
    directivo_id = request.GET.get('id')  # ID del directivo que estamos editando
    print (directivo_id)
    if correo:
        # Excluir el `directivo_id` solo en `Directivos`
        if directivo_id:
            existe = (
                Directivos.objects.filter(Correo=correo).exclude(idDirectivos=directivo_id).exists() or
                Profesor.objects.filter(Correo=correo).exists()
            )
        else:
            existe = (
                Directivos.objects.filter(Correo=correo).exists() or
                Profesor.objects.filter(Correo=correo).exists()
            )
        return JsonResponse({'existe': existe})
    
    # Respuesta si el `correo` no se proporciona
    return JsonResponse({'error': 'Correo no proporcionado'}, status=400)
    