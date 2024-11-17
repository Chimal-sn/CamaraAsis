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
    const fechainicio = document.getElementById('id_FechaInicio').value;
    const fechafin = document.getElementById('id_FechaFin').value;

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



async function validareditar(event) {
    event.preventDefault(); // Prevenir el envío del formulario

    const nombre = document.getElementById('id_nombre').value;  // Asegúrate de que este campo tenga el ID correcto
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const id = document.getElementById('edit_id').value;  // Obtener el campo edit_id (puede ser null si no existe)
    const fechainicio = document.getElementById('id_fecha_inicio').value;
    const fechafin = document.getElementById('id_fecha_fin').value;


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

document.addEventListener('DOMContentLoaded', function () {
    const inputBusqueda = document.getElementById('busqueda-periodo');
    const contenedorPeriodos = document.getElementById('periodos-container');

    inputBusqueda.addEventListener('keyup', function () {
        const query = this.value;

        fetch(`/buscar-periodos/?q=${query}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            contenedorPeriodos.innerHTML = ''; // Limpia los resultados anteriores

            // Añade los nuevos resultados dinámicamente
            data.forEach(periodo => {
                const item = document.createElement('div');
                item.className = 'grid-item';
                item.innerHTML = `
                    <h4>${periodo.nombre}</h4>
                    <p><strong>Fecha de Inicio:</strong> ${periodo.fechainicio}</p>
                    <p><strong>Fecha Fin:</strong> ${periodo.fechafin}</p>
                    <div class="grid-actions">
                        <a href="/EliminarPeriodo/${periodo.id}" class="delete-btn" onclick="return confirm('¿Estás seguro de que deseas eliminar este periodo?')">Eliminar</a>
                        <button class="update-btn" onclick="openModal(
                            ${periodo.id},
                            '${periodo.nombre}',
                            '${periodo.fechainicio}',
                            '${periodo.fechafin}'
                        )">Actualizar</button>
                    </div>
                `;
                contenedorPeriodos.appendChild(item);
            });      
        });
    });
});
