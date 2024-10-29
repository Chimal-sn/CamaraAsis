from functools import wraps
from django.shortcuts import render,redirect,get_object_or_404
from ..models import Profesor, Horario, DiaAsistencia 
from ..forms import JustificacionForm

def user_is_professor(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Obtener el rol del usuario desde la sesión
        rol = request.session.get('user_rol')
        
        # Verificar si el rol es 'Profesor'
        if rol == "Profesor":
            return view_func(request, *args, **kwargs)
        else:
            return render(request,"No_acceso.html")
    
    return _wrapped_view

@user_is_professor
def HomeProfesor(request):
    return render(request, "Profesor/HomeProfesor.html")

@user_is_professor 
def Asistencias(request):
    form = JustificacionForm()
    id = request.session.get('user_id')
    profesor =  Profesor.objects.get(idProfesor=id)
    
    asistencias = DiaAsistencia.objects.all()
    horarios = Horario.objects.all()
    
    horarios_pro = horarios.filter(idProfesor=profesor)
    asistencias_pro = asistencias.filter(idHorario__in=horarios_pro)
    
    return render(request, 'Profesor/Asistencias.html',{'profesor': profesor, 'asistencias': asistencias_pro,'form': form})



def justificacion_view(request, asistencia_id):
    asistencia = get_object_or_404(DiaAsistencia, id=asistencia_id)
    
    if request.method == 'POST':
        form = JustificacionForm(request.POST)
        if form.is_valid():
            justificacion = form.save(commit=False)
            justificacion.idDiaAsistencia = asistencia  # Asignar la asistencia correspondiente
            justificacion.estado = "Pendiente"
            justificacion.save()  # Guardar la justificación en la base de datos
            return redirect("Asistencias")
    else:
        form = JustificacionForm()
    profesor =  Profesor.objects.get(idProfesor=id)
    asistencias = DiaAsistencia.objects.filter(idProfesor = profesor)
    return render(request, 'Profesor/Asistencias.html',{'profesor': profesor, 'asistencias': asistencias,'form': form})
