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
                    return redirect('HomeDirectivo')
                else:
                    
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
                            
                            return redirect('IniciarSesion')  # Redirige si la contraseña es incorrecta
                    except Administrador.DoesNotExist:
                        return redirect('IniciarSesion')
        
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
        profesor.imagen_rostro = file_path
        profesor.save()
        
        return JsonResponse({'status': 'success'})

    return render(request, 'CapturaImagen.html')

def Foto(request):
    return render(request, 'Profesor/subirimagen.html')



def subirfoto(request):
    if request.method == 'POST' and request.FILES.get('image_data'):
        image_file = request.FILES['image_data']
        
        # Verificar que el archivo es JPEG
        if not image_file.name.endswith('.jpg') and not image_file.content_type == 'image/jpeg':
            return JsonResponse({'status': 'error', 'message': 'Solo se aceptan imágenes en formato JPEG.'}, status=400)
        
        # Recupera el id del directivo desde la sesión
        iddirectivo = request.session.get('user_id')
        
        # Obtén el objeto Profesor
        profesor = Profesor.objects.get(idProfesor=iddirectivo)

        # Convierte idProfesor a cadena para usarlo en la ruta
        id_profesor_str = "rostro_" + str(profesor.idProfesor)

        # Define el path donde quieres guardar la imagen
        file_path = os.path.join(settings.MEDIA_ROOT, 'rostros', f'{id_profesor_str}.jpg')

        # Guarda la imagen en el sistema de archivos
        with open(file_path, 'wb') as img_file:
            for chunk in image_file.chunks():
                img_file.write(chunk)

        # Actualiza el campo `imagen_rostro` del modelo `Profesor`
        profesor.imagen_rostro = file_path
        profesor.save()
        
        return JsonResponse({'status': 'success'})

    return render(request, 'Profesor/subirimagen.html')


def lista(request):
    return render(request, 'Inicio/lista.html')

import face_recognition
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.utils.decorators import method_decorator
from ..models import Profesor, Horario, DiaAsistencia
from datetime import datetime, timedelta
from pathlib import Path
from PIL import Image
import os
import base64
import json
from io import BytesIO

# Directorio para almacenar imágenes capturadas
BASE_DIR = Path(__file__).resolve().parent
CAPTURED_IMAGES_DIR = os.path.join(BASE_DIR, 'captured_faces')
if not os.path.exists(CAPTURED_IMAGES_DIR):
    os.makedirs(CAPTURED_IMAGES_DIR)

# Diccionario para almacenar codificaciones dinámicas
profesor_encodings = {}


def save_captured_face(profesor, image_data):
    """
    Guarda la imagen capturada en el disco para entrenar el modelo dinámicamente.
    """
    filename = os.path.join(CAPTURED_IMAGES_DIR, f"{profesor.idProfesor}_{now().strftime('%Y%m%d_%H%M%S')}.jpg")
    with open(filename, 'wb') as f:
        f.write(image_data)
    print(f"Imagen capturada guardada para {profesor.Nombre}: {filename}")


def update_encodings(profesor):
    """
    Genera y actualiza las codificaciones del profesor basado en sus imágenes almacenadas.
    """
    global profesor_encodings
    encodings = []
    if profesor.imagen_rostro:
        try:
            img = face_recognition.load_image_file(profesor.imagen_rostro)
            encoding = face_recognition.face_encodings(img)
            if encoding:
                encodings.append(encoding[0])
        except Exception as e:
            print(f"Error procesando la imagen {profesor.imagen_rostro}: {e}")
    profesor_encodings[profesor.idProfesor] = encodings
    print(f"Codificaciones actualizadas para {profesor.Nombre}")
    


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
            # Actualizar las codificaciones del profesor
            if profesor.idProfesor not in profesor_encodings:
                update_encodings(profesor)

            # Comparar con las codificaciones almacenadas
            encodings = profesor_encodings.get(profesor.idProfesor, [])
            results = any(face_recognition.compare_faces(encodings, captured_encoding, tolerance=0.5))
            if results:
                save_captured_face(profesor, image_data)  # Guardar la imagen capturada
                # Verificar horario y asistencia
                horario = Horario.objects.filter(idProfesor=profesor).last()
                if not horario:
                    return JsonResponse({'match': True, 'profesor_id': profesor.Nombre, 'message': 'Sin horario asignado.'})

                hoy = now().date()
                dia = hoy.weekday()
                hora_actual = now().time()
                
                asistencias_hoy = DiaAsistencia.objects.filter(fecha_y_hora__date=hoy, idHorario=horario, )
                if asistencias_hoy.exists():
                    print(f"Ya se encontró asistencia para el profesor {profesor.Nombre} hoy")
                    return JsonResponse({'match': True, 'profesor_id': profesor.Nombre})
                
                # Obtener el horario del día correspondiente
                hora_horario = getattr(horario, ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'][dia], None)

                if hora_horario:
                    rango_superior = (datetime.combine(hoy, hora_horario) + timedelta(minutes=15)).time()
                    rango_inferior = (datetime.combine(hoy, hora_horario) - timedelta(minutes=5)).time()

                    if rango_inferior <= hora_actual <= rango_superior:
                        asistencia = DiaAsistencia(Tipo="Asistencia", idHorario=horario)
                    else:
                        asistencia = DiaAsistencia(Tipo="Retardo", idHorario=horario)
                    asistencia.save()

                    return JsonResponse({'match': True, 'profesor_id': profesor.Nombre, 'asistencia': asistencia.Tipo})

                return JsonResponse({'match': True, 'profesor_id': profesor.Nombre, 'message': 'Sin horario para hoy.'})

        # Si no se encontró coincidencia
        return JsonResponse({'match': False, 'message': 'No se encontró coincidencia con los rostros almacenados.'})

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

