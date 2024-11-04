from django.http import HttpResponse, JsonResponse
from ..models import Directivos, Profesor, DiaAsistencia, Horario ,Administrador
from django.shortcuts import render,redirect,get_object_or_404
from ..forms import DirectivoLoginForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import face_recognition
from functools import wraps
from django.utils import timezone
from django.conf import settings
import os
from datetime import datetime, timedelta, time


# ------------------------------ AREA DEL MENU PRINCIPAL ------------------------------#

# Create your views here.
def index(request):
    return render(request, 'index.html')



def IniciarSesion(request):
    form_directivo = DirectivoLoginForm()

    if request.method == 'POST':
        form_directivo = DirectivoLoginForm(request.POST)
        if form_directivo.is_valid():
            matricula = form_directivo.cleaned_data['Matricula']
            contrasena = form_directivo.cleaned_data['contraseña']
            
            try:
                # Primero busca al Directivo
                directivo = Directivos.objects.get(Matricula=matricula)
                if (contrasena == directivo.Contrasena):  # Validación de contraseña
                    request.session['user_id'] = directivo.idDirectivos
                    request.session['user_rol'] = "Directivo"
                    messages.success(request, f"Bienvenido {directivo.idDirectivos}")
                    return redirect('HomeDirectivo')
                else:
                    messages.error(request, "Contraseña incorrecta")
                    return redirect('IniciarSesion')  # Redirige si la contraseña es incorrecta
            except Directivos.DoesNotExist:
                # Si no es Directivo, busca al Profesor
                try:
                    profesor = Profesor.objects.get(Matricula=matricula)
                    if  (contrasena == profesor.Contrasena):  # Validación de contraseña
                        request.session['user_id'] = profesor.idProfesor
                        request.session['user_rol'] = "Profesor"
                        messages.success(request, f"Bienvenido {profesor.idProfesor}")
                        return redirect('HomeProfesor')
                    else:
                        messages.error(request, "Contraseña incorrecta")
                        return redirect('IniciarSesion')  # Redirige si la contraseña es incorrecta
                except Profesor.DoesNotExist:
                    # Si no encuentra ni directivo ni profesor
                    try:
                        administrador = Administrador.objects.get(Matricula=matricula)
                        if  (contrasena == administrador.Contrasena):  # Validación de contraseña
                            request.session['user_id'] = administrador.id
                            request.session['user_rol'] = "Administrador"
                            return redirect('InicioAdministrador')
                        else:
                            messages.error(request, "Contraseña incorrecta")
                            return redirect('IniciarSesion')  # Redirige si la contraseña es incorrecta
                    except Administrador.DoesNotExist:
                        messages.error(request,"Matricula o Contraseña incorrecta")
        
    return render(request, 'Inicio/IniciarSesion.html', {'form_directivo': form_directivo})




# ------------------------------ CAMARA ------------------------------#



def FotoCara(request):
    return render(request, "Profesor/CapturaImagen.html")


def upload_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        img_data = base64.b64decode(imgstr)
        
        iddirectivo = request.session.get('user_id')
        
        profesor = Profesor.objects.get(idProfesor=iddirectivo)

        # Convierte idProfesor a cadena para usarlo en la ruta
        id_profesor_str = "rostro_" + str(profesor.idProfesor)

        # Define el path donde quieres guardar la imagen
        file_path = os.path.join(settings.MEDIA_ROOT, 'rostros', f'{id_profesor_str}.{ext}')

        
        # Guarda la imagen en el sistema de archivos
        with open(file_path, 'wb') as img_file:
            img_file.write(img_data)

        # Actualiza el campo `imagen_rostro` del modelo `Profesor`
          # Aquí debes seleccionar el profesor correcto
        profesor.imagen_rostro = file_path
        profesor.save()
        
        return JsonResponse({'status': 'success'})

    return render(request, 'CapturaImagen.html')


def lista(request):
    return render(request, 'Inicio/lista.html')

import face_recognition
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models import Profesor
from io import BytesIO
import base64
from PIL import Image
import json


@csrf_exempt
def compare_faces(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data.get('imageData').split(',')[1]  # Extraer la imagen en base64
        image_data = base64.b64decode(image_data)

        # Convertir la imagen a formato RGB para face_recognition
        image = Image.open(BytesIO(image_data))
        image = image.convert('RGB')
        image_np = np.array(image)
        
        # Obtener las codificaciones de la imagen capturada
        captured_encoding = face_recognition.face_encodings(image_np)
        if not captured_encoding:
            return JsonResponse({'match': False, 'message': 'No se detectó un rostro en la imagen capturada.'})

        captured_encoding = captured_encoding[0]
        
        # Obtener los profesores y comparar sus imágenes
        profesores = Profesor.objects.all()
        for profesor in profesores:
            # Cargar la imagen del rostro del profesor
            try:
                rostro_imagen = face_recognition.load_image_file(profesor.imagen_rostro)
                rostro_encoding = face_recognition.face_encodings(rostro_imagen)
                if not rostro_encoding:
                    continue
                rostro_encoding = rostro_encoding[0]
            except Exception as e:
                print(f"Error al cargar la imagen del profesor {profesor.Nombre}: {e}")
                continue

            # Comparar las codificaciones
            results = face_recognition.compare_faces([rostro_encoding], captured_encoding)
            if results[0]:
                try:
                    horario = Horario.objects.filter(idProfesor=profesor).last()
                    if not horario:
                        print(f"No se encontró un horario para el profesor {profesor.Nombre}")
                        return JsonResponse({'match': True, 'profesor_id': profesor.Nombre})

                    hoy = timezone.now().date()  # Obtener solo la parte de la fecha actual (sin la hora)
                    dia = hoy.weekday()
                    hora_actual = timezone.now().time()

                    # Filtrar las asistencias del profesor registradas hoy
                    asistencias_hoy = DiaAsistencia.objects.filter(fecha_y_hora__date=hoy, idHorario=horario, )
                    if asistencias_hoy.exists():
                        print(f"Ya se encontró asistencia para el profesor {profesor.Nombre} hoy")
                        return JsonResponse({'match': True, 'profesor_id': profesor.Nombre})

                    
                    # Obtener el horario para el día de hoy
                    hora_horario = None
                    if dia == 0:
                        hora_horario = horario.Lunes
                    elif dia == 1:
                        hora_horario = horario.Martes
                    elif dia == 2:
                        hora_horario = horario.Miercoles
                    elif dia == 3:
                        hora_horario = horario.Jueves
                    elif dia == 4:
                        hora_horario = horario.Viernes
                    elif dia  == 5:
                        hora_horario = horario.Lunes


                    if hora_horario is not None:
                        rango_tiempo_superior = (datetime.combine(hoy, hora_horario) + timedelta(minutes=15)).time()
                        rango_tiempo_inferior = (datetime.combine(hoy, hora_horario) - timedelta(minutes=5)).time()

                        if rango_tiempo_inferior <= hora_actual <= rango_tiempo_superior:
                            print("El profesor está dentro del rango de horario permitido.")
                            Dasistencia = DiaAsistencia (Tipo="Asistencia", idHorario=horario)
                            Dasistencia.save()
                            return JsonResponse({'match': True, 'profesor_id': profesor.Nombre,  'asistencia': True})

                        else:
                            Dasistencia = DiaAsistencia(Tipo="Retardo", idHorario=horario)
                            Dasistencia.save()
                            print("El profesor está fuera del rango de horario permitido.")
                            return JsonResponse({'match': True, 'profesor_id': profesor.Nombre,  'asistencia': True})

                    else:
                        print("No hay horario para el profesor hoy")
                        return JsonResponse({'match': True, 'profesor_id': profesor.Nombre})
                except Horario.DoesNotExist:
                    print(f"No se encontró un horario para el profesor {profesor.Nombre}")
                
                return JsonResponse({'match': True, 'profesor_id': profesor.Nombre})

        # Si no se encontró ninguna coincidencia
        return JsonResponse({'match': False})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# ------------------------------ ROLES ------------------------------#


def get_session_data(request):
    # Recuperar datos de la sesión
    integer_value = request.session.get('ID', 'No integer found')
    string_value = request.session.get('Rol', 'No string found')
    return HttpResponse(f"ID value: {integer_value}, Rol value: {string_value}")    

def clear_session_data(request):
    # Eliminar datos específicos de la sesión
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_rol' in request.session:
        del request.session['user_rol']
    return HttpResponse("Datos de la sesión eliminados.")

import os
import subprocess
from django.http import FileResponse, HttpResponse
from django.conf import settings
from datetime import datetime

def backup_database(request):
    # Configura el nombre y ruta del archivo de respaldo
    backup_dir = os.path.join(settings.BASE_DIR, "backups")
    os.makedirs(backup_dir, exist_ok=True)  # Crear el directorio si no existe
    backup_file = os.path.join(backup_dir, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql")

    # Ejecuta el comando de respaldo para MySQL
    try:
        command = [
            "mysqldump",
            "--skip-column-statistics",  # Ignorar la recopilación de estadísticas de columna
            "--routines",  # Incluye procedimientos almacenados
            "--triggers",  # Incluye triggers
            "-u", settings.DATABASES['default']['USER'],
            "-h", settings.DATABASES['default']['HOST'],
        ]
        
        # Verifica si se requiere una contraseña (aunque esté vacía)
        if settings.DATABASES['default']['PASSWORD']:
            command.insert(3, f"-p{settings.DATABASES['default']['PASSWORD']}")
        
        # Agrega el nombre de la base de datos 'listas'
        command.append('listas')

        # Ejecuta el comando y guarda el respaldo
        with open(backup_file, "w") as output_file:
            result = subprocess.run(command, stdout=output_file, stderr=subprocess.PIPE)

        # Verifica si hubo errores
        if result.returncode != 0:
            error_message = result.stderr.decode()  # Obtiene el mensaje de error
            return HttpResponse(f"Error al generar el respaldo: {error_message}", status=500)

        # Envía el archivo de respaldo al usuario
        response = FileResponse(open(backup_file, "rb"), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(backup_file)}"'
        return response

    except Exception as e:
        return HttpResponse(f"Error al generar el respaldo: {str(e)}", status=500)
