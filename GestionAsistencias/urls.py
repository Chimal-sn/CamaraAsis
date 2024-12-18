from django.urls import path
from .Views import view_Directivo, views, view_Profesor, view_Administrador
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.index, name = 'Inicio'),
    
    
    path('Ingresar/',view_Directivo.crear_profesor, name = "RegistrarProfesor"),
    path('homedirectivo/', view_Directivo.CasaDirectivo, name= "HomeDirectivo"),
    path('Periodo/', view_Directivo.Reporte, name = "Periodo"),  
    path('GestionProfesores/', view_Directivo.GestionProfesores, name = "GestionProfesores"),   
    path('EliminarProfesor/<int:id>',  view_Directivo.BorrarProfesor, name = "EliminarProfesor"),
    path('EditarProfesor/<int:id>', view_Directivo.EditarProfesor, name = "EditarProfesor"),
    path('CerrarSesionDirectivo/', view_Directivo.CerrarSesionDirectivo, name = "CerrarSesionDirectivo"),
    path('GestionHorarios/<int:id>', view_Directivo.GestionHorarios, name=  "GestionHorarios"),
    path('EliminarHorario/<int:id>/<int:idPro>',  view_Directivo.EliminarHorario, name = "EliminarHorario"),
    path('CrearHorario/<int:id>', view_Directivo.CrearHorario, name = "CrearHorario"  ),
    path('GestionHorarios/EditarHorario/<int:id>',view_Directivo.EditarHorario,  name = "EditarHorario"),
    path('GestionPeriodos/', view_Directivo.GestionPeriodos,  name = "GestionPeriodos"),
    path('EliminarPeriodo/<int:id>', view_Directivo.EliminarPeriodo, name = "EliminarPeriodo"),
    path('CrearPeriodo',view_Directivo.CrearPeriodo, name =  "CrearPeriodo"),
    path('EditarPeriodo/<int:id>',view_Directivo.EditarPeriodo, name =  "EditarPeriodo"),
    path('buscar-profesores/',view_Directivo.buscar_profesores, name = "BuscarProfesores"),
    path('buscar-periodos/',view_Directivo.buscar_periodos, name = "BuscarPeriodos"),
    path('ReportePDFDirec/',view_Directivo.generar_reporte_pdf, name = "ReportePDFDirec"),
    path('ReporteExcel/',view_Directivo.generar_reporte_excel, name = "ReporteExcel"),
    
    
    path('CrearPDF/<int:id>/<int:idHorario>', view_Directivo.crear_pdf, name = "CrearPDF"),
    path('EliminarPDF/<int:id>/<int:idPro>', view_Directivo.EliminarPDF, name = "EliminarPDF"),
    path('EditarPDF/<int:id>/<int:idPro>', view_Directivo.EditarPDF, name = "EditarPDF"),
    
    path('Justificantes/', view_Directivo.Justificante, name=  "Justificantes"),
    path('AceptarJustificante/<int:id>', view_Directivo.AceptarJustificante, name=   "AceptarJustificante"),
    path('validar-nombre/',view_Directivo.validar_nombre, name = "validar-nombre"),
    path('validar-fechas/',view_Directivo.validar_fechas, name ="validar-fechas"),
    path('validar-matricula-profesor/',view_Directivo.validar_matricula_profesor, name = "validar-matricula-profesor"),
    path('validar-correo-profesor/',view_Directivo.validar_correo_profesor, name = "validar-correo-profesor"),
    path('validar-periodo-profesor/', view_Directivo.validar_periodo_profesor, name='validar_periodo_profesor'),






    path('backup_database',view_Administrador.backup_database, name = "backup_database"),

    
    path('HomeProfesor/', view_Profesor.HomeProfesor, name="HomeProfesor"),
    path('Asistencias/', view_Profesor.Asistencias, name = 'Asistencias'),
    path('justificar/<int:asistencia_id>/', view_Profesor.justificacion_view, name='justificacion_view'),
    path('CerrarSesionProfesor/', view_Profesor.CerrarSesionProfesor, name = "CerrarSesionProfesor"),
    
    
    
    path('upload/', views.upload_image, name='upload_image'),
    path('SubirFoto/', views.FotoCara, name= 'FotoCara'),
    path('compare_faces/', views.compare_faces, name='compare_faces'),
    path('lista/', views.lista, name = 'lista'),
    path('eliminar/', views.clear_session_data, name = "borrar"),
    path('iniciar/', views.IniciarSesion, name='IniciarSesion'),
    path('SubirCara',views.subirfoto, name = "SubirCara"),
    path('Si',views.Foto, name = "Foto"),
    
    
    
    path('CerrarSesionAdmin',view_Administrador.CerrarSesionAdmin, name = "CerrarSesionAdmin"),
    path('GestionDirectivos/', view_Administrador.GestionarDirectivo, name = "GestionarDirectivos"),
    path('EliminarDirectivo/<int:id>', view_Administrador.BorrarDirectivo, name = "EliminarDirectivo"),
    path('InicioAdministrador/',view_Administrador.InicioAdmnistrador, name = "InicioAdministrador"),
    path('EditarDirectivo/<int:id>', view_Administrador.EditarDirectivo, name = "EditarDirectivo"),
    path('CrearDirectivo', view_Administrador.crear_directivo, name = "CrearDirectivo"),
    path('ReporteAdministrador/', view_Administrador.ReporteAsis, name ="ReporteAdministrador"),
    path('reporte-pdf/', view_Administrador.generar_reporte_pdf, name='reporte_pdf'),
    path('validar-matricula/', view_Administrador.validar_matricula, name='validar_matricula'),
    path('validar-correo/', view_Administrador.validar_correo, name='validar_correo'),
    
    path('buscar-directivos/', view_Administrador.buscar_directivos, name='buscar_directivos'),

]


