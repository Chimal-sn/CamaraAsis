CREATE DATABASE listas;
show tables;

select * from myapp_project;

select *from gestionasistencias_directivos;

select *from gestionasistencias_profesor;

describe gestionasistencias_profesor;

select *from gestionasistencias_diaasistencia;

describe gestionasistencias_diaasistencia;

select *from gestionasistencias_horario;

describe gestionasistencias_horario;

select *from gestionasistencias_retardo;

select *from gestionasistencias_justificacion;


select *from gestionasistencias_PeriodoEscolar;

select *from gestionasistencias_Administrador;


INSERT INTO gestionasistencias_directivos (Nombre, Apellidos, Matricula, Correo, Contrasena) VALUES
('Juan', 'Pérez', '12345678', 'juan.perez@example.com', '123'),
('María', 'González', '87654321', 'maria.gonzalez@example.com', '123');


INSERT INTO `listas`.`gestionasistencias_profesor` (`idProfesor`, `Nombre`, `Apellidos`, `Contrasena`, `imagen_rostro`, `idDirectivos_id`,`Matricula`,`Correo`) 
VALUES 
('1', 'Sony', 'dasdas', '1234', 'C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_1.jpeg', '1','hola','no'),
('2', 'Elon', 'Musk', '123', 'C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_2.jpeg', '1','ELMSK','no'),
('3', 'Vegetaa', 'Luque', '123', 'C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_3.jpeg', 'VG777','si','no');


INSERT INTO gestionasistencias_pdfhorario (FechaModificacion, Nombre, horario_pdf, idHorario_id)
VALUES ('2024-11-12 10:00:00', 'Horario Matemáticas', 'matematicas_horario.pdf', 28);



INSERT INTO gestionasistencias_PeriodoEscolar (Nombre, FechaInicio, FechaFin) VALUES
('Otoño 2024', '2024-01-15 08:00:00', '2024-04-30 18:00:00'),
('Verano 2024', '2024-05-01 08:00:00', '2024-08-31 18:00:00');

INSERT INTO gestionasistencias_horario (Lunes, Martes, Miercoles, Jueves, Viernes, idProfesor_id, idPeriodo_id) VALUES 
('08:30:00', NULL, NULL, NULL, NULL, 1, 2);

INSERT INTO gestionasistencias_diaasistencia (fecha_y_hora, Tipo, idHorario_id) VALUES
('2024-09-25 08:15:00', 'Retardo',32);


('2024-09-25 17:00:00', 'Retardo', 2);


INSERT INTO gestionasistencias_Administrador (nombre, Matricula, Contrasena) 
VALUES ('Carlos Martínez', 'CM', 'admin1');



show tables;


UPDATE gestionasistencias_directivos
SET idDirectivos = 2
WHERE idDirectivos = 4;


UPDATE gestionasistencias_diaasistencia
SET Tipo = "Retardo"
WHERE id = 4;

UPDATE gestionasistencias_profesor
SET Matricula = "P55"
WHERE idProfesor = 4;

UPDATE gestionasistencias_profesor
SET nombre = "alberg"
WHERE idProfesor = 4;


UPDATE gestionasistencias_diaasistencia
SET Tipo = "Retardo"
WHERE id = 4;

delete from  gestionasistencias_justificacion where idJustificacion = 1;

delete from  gestionasistencias_diaasistencia where id = 14;

select *from gestionasistencias_justificacion;


delete from  gestionasistencias_justificacion where idDiaAsistencia_id = 14;


delete from  gestionasistencias_justificacion where idJustificacion = 8;

delete from gestionasistencias_pdfhorario where idPDFhorario = 11;