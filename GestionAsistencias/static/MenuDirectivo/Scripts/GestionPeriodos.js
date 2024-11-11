function openModal(id, nombre, fechainicio, fechafin) {

    document.getElementById('edit_id').value = id;
    document.getElementById('editForm').action = `/EditarPeriodo/${id}`;
    document.getElementById('id_nombre').value = nombre;
    document.getElementById('id_fecha_inicio').value = fechainicio; 
    document.getElementById('id_fecha_fin').value = fechafin;
    


    document.getElementById('editModal').style.display = 'flex';
}


async function validarNombre(event) {
    event.preventDefault(); // Prevenir el envío del formulario

    const nombre = document.getElementById('id_Nombre').value;  // Asegúrate de que este campo tenga el ID correcto
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const editId = document.getElementById('edit_id');  // Obtener el campo edit_id (puede ser null si no existe)
    const fechainicio = document.getElementById('id_FechaInicio');
    const fechafin = document.getElementById('id_FechaFin');

    // Si el campo edit_id no existe o no tiene valor, es un formulario de creación
    const id = editId && editId.value ? editId.value : '';

    try {
        // Realizar la validación en el servidor con el nombre y el id
        const response = await fetch(`/validar-nombre/?nombre=${encodeURIComponent(nombre)}&id=${encodeURIComponent(id)}`);
        const data = await response.json();

        if (data.existe) {
            modal.style.display = 'flex';
            mensaje.innerText = "Periodo ya está registrado";
            return false;  // Detener el envío del formulario si existe el nombre
        }
    } catch (error) {
        console.error('Error al validar el nombre:', error);
        alert("Ocurrió un error al validar el nombre. Inténtalo de nuevo.");
        return false;  // Detener el envío del formulario si ocurre un error
    }


    try {
        // Realizar la validación en el servidor con la fecha de inicio y fin
        const response = await fetch(`/validar-fechas/?fecha_inicio=${encodeURIComponent(fechainicio)}&fecha_final=${encodeURIComponent(fechafin)}`);
        const data = await response.json();
    
        if (!data.es_valido) {
            modal.style.display = 'flex';
            mensaje.innerText = "Las fechas son incorrectas";
            return false;
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
    }


    

    // Si todo está bien, permitir el envío del formulario
    event.target.submit();
}





function closeModal() {
    document.getElementById('editModal').style.display = 'none';
}



function abrirCrear(){
    document.getElementById('CrearModal').style.display = 'flex';
}

function CerrarModalCrear() {
    document.getElementById('CrearModal').style.display = 'none';
}


function CerrarAlerta(){
    document.getElementById('Alerta').style.display = 'none';
}