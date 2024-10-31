from django.urls import path
from .Views import views, view_Profesor, view_Director, view_Administrador
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.index, name = 'Inicio'),
    
    
    path('Ingresar/',view_Director.crear_profesor, name = "RegistrarProfesor"),
    path('homedirectivo/', view_Director.CasaDirectivo, name= "HomeDirectivo"),
    path('Periodo/', view_Director.periodo, name = "Periodo"),  
    path('GestionProfesores/', view_Director.GestionProfesores, name = "GestionProfesores"),   
    path('EliminarProfesor/<int:id>/',  view_Director.BorrarProfesor, name = "EliminarProfesor"),
    path('EditarProfesor/<int:id>/', view_Director.EditarProfesor, name = "EditarProfesor"),
    
    
    path('HomeProfesor/', view_Profesor.HomeProfesor, name="HomeProfesor"),
    path('Asistencias/', view_Profesor.Asistencias, name = 'Asistencias'),
    path('justificar/<int:asistencia_id>/', view_Profesor.justificacion_view, name='justificacion_view'),
    path('CerrarSesionProfesor', view_Profesor.CerrarSesionProfesor, name = "CerrarSesionProfesor"),
    
    
    path('upload/', views.upload_image, name='upload_image'),
    path('SubirFoto/', views.FotoCara, name= 'FotoCara'),
    path('compare_faces/', views.compare_faces, name='compare_faces'),
    path('lista/', views.lista, name = 'lista'),
    path('eliminar/', views.clear_session_data, name = "borrar"),
    path('iniciar/', views.IniciarSesion, name='IniciarSesion'),
    
    
    
    path('CerrarSesionAdmin',view_Administrador.CerrarSesionAdmin, name = "CerrarSesionAdmin"),
    path('GestionDirectivos/', view_Administrador.GestionarDirectivo, name = "GestionarDirectivos"),
    path('EliminarDirectivo/<int:id>', view_Administrador.BorrarDirectivo, name = "EliminarDirectivo"),
    path('InicioAdministrador/',view_Administrador.InicioAdmnistrador, name = "InicioAdministrador"),
    path('EditarDirectivo/<int:id>', view_Administrador.EditarDirectivo, name = "EditarDirectivo"),
    path('CrearDirectivo', view_Administrador.crear_directivo, name = "CrearDirectivo"),
    path('ReporteAdministrador/', view_Administrador.ReporteAsis, name ="ReporteAdministrador")
    
    
    

]


