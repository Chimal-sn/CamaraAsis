
function openModal(id, nombre, apellido, matricula, contrasena, correo) {
    document.getElementById('editForm').action = `/EditarDirectivo/${id}`;
    document.getElementById('id_nombre').value = nombre;
    document.getElementById('id_apellido').value = apellido;
    document.getElementById('id_matricula').value = matricula;
    document.getElementById('id_contrasena').value = contrasena;
    document.getElementById('id_correo').value = correo;
    document.getElementById('edit_id').value = id;

    document.getElementById('editModal').style.display = 'flex';
}


function closeModal() {
    const modal = document.getElementById('editModal');
    modal.style.display = 'none'; // Solo cerrar el modal si el formulario es válido y se envió correctamente
}




async function validateMatricula(event) {
    // Prevenir el comportamiento por defecto para que no se envíe el formulario inmediatamente
    event.preventDefault();

    const matriculaInput = document.getElementById('id_Matricula').value;
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const formulario = document.getElementById('crearDirectivoForm');
    const correoInput = document.getElementById('id_Correo').value;
    const directivoId = document.getElementById('edit_id').value;


   // Validación de la matrícula
    try {
        const response = await fetch(`/validar-matricula/?matricula=${encodeURIComponent(matriculaInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            modal.style.display = 'flex';
            mensaje.innerText = "La matrícula ya está registrada";
            return false;  // Detener el envío del formulario
        }
    } catch (error) {
        console.error('Error al validar la matrícula:', error);
        alert("Ocurrió un error al validar la matrícula. Inténtalo de nuevo.");
        return false;  // Detener el envío del formulario si hay un error
    }

    // Validación del correo
    try {
        const response = await fetch(`/validar-correo/?correo=${encodeURIComponent(correoInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            modal.style.display = 'flex';
            mensaje.innerText = "El correo ya está registrado";
            return false;  // Detener el envío del formulario
        }
    } catch (error) {
        console.error('Error al validar el correo:', error);
        alert("Ocurrió un error al validar el correo. Inténtalo de nuevo.");
        return false;  // Detener el envío del formulario si hay un error
    }

    // Si ambas validaciones son exitosas, proceder con el envío del formulario
    formulario.submit();
}




async function validarEditar(event) {
    // Prevenir el comportamiento por defecto para que no se envíe el formulario inmediatamente
    event.preventDefault();

    const matriculaInput = document.getElementById('id_matricula').value;
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const formulario = document.getElementById('editForm');
    const correoInput = document.getElementById('id_correo').value;
    const directivoId = document.getElementById('edit_id').value;


   // Validación de la matrícula
    try {
        const response = await fetch(`/validar-matricula/?matricula=${encodeURIComponent(matriculaInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            modal.style.display = 'flex';
            mensaje.innerText = "La matrícula ya está registrada";
            return false;  // Detener el envío del formulario
        }
    } catch (error) {
        console.error('Error al validar la matrícula:', error);
        alert("Ocurrió un error al validar la matrícula. Inténtalo de nuevo.");
        return false;  // Detener el envío del formulario si hay un error
    }

    // Validación del correo
    try {
        const response = await fetch(`/validar-correo/?correo=${encodeURIComponent(correoInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            modal.style.display = 'flex';
            mensaje.innerText = "El correo ya está registrado";
            return false;  // Detener el envío del formulario
        }
    } catch (error) {
        console.error('Error al validar el correo:', error);
        alert("Ocurrió un error al validar el correo. Inténtalo de nuevo.");
        return false;  // Detener el envío del formulario si hay un error
    }

    // Si ambas validaciones son exitosas, proceder con el envío del formulario
    formulario.submit();
}


function CerrarAlerta(){
    document.getElementById('Alerta').style.display = 'none';
}



function abrirCrear(){
    document.getElementById('CrearModal').style.display = 'flex';
}

function CerrarModalCrear() {
    const modal = document.getElementById('CrearModal');
    modal.style.display = 'none'; // Solo cerrar el modal si el formulario es válido y se envió correctamente
}