
function openModal(id, nombre, apellido, matricula, contrasena, correo) {
    document.getElementById('editForm').action = `/EditarProfesor/${id}`;
    document.getElementById('id_nombre').value = nombre;
    document.getElementById('id_apellido').value = apellido;
    document.getElementById('id_matricula').value = matricula;
    document.getElementById('id_contrasena').value = contrasena;
    document.getElementById('id_correo').value = correo;
    document.getElementById('editModal').style.display = 'flex';
    document.getElementById('edit_id').value = id;

}




function closeModal() {
    document.getElementById('editModal').style.display = 'none';
}




async function validarCrear(event) {
    event.preventDefault();

    const matriculaInput = document.getElementById('id_Matricula').value;
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const directivoId = document.getElementById('edit_id') ? document.getElementById('edit_id').value : '';
    const correoInput = document.getElementById('id_Correo').value;

    // Validación de la matrícula
    try {
        const response = await fetch(`/validar-matricula-profesor/?matricula=${encodeURIComponent(matriculaInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Matrícula ya registrada");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "La matrícula ya está registrada";
            return false;
        }
    } catch (error) {
        console.error('Error al validar la matrícula:', error);
        alert("Ocurrió un error al validar la matrícula. Inténtalo de nuevo.");
        return false;
    }

    // Validación del correo
    try {
          // Asegúrate de que el campo correo esté en el HTML
        const response = await fetch(`/validar-correo-profesor/?correo=${encodeURIComponent(correoInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Correo ya registrado");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "El correo ya está registrado";
            return false;
        }
    } catch (error) {
        console.error('Error al validar el correo:', error);
        alert("Ocurrió un error al validar el correo. Inténtalo de nuevo.");
        return false;
    }

    event.target.submit();
}


async function validareditar(event) {
    event.preventDefault();

    const matriculaInput = document.getElementById('id_matricula').value;
    const modal = document.getElementById('Alerta');
    const mensaje = document.getElementById('Mensaje');
    const directivoId = document.getElementById('edit_id') ? document.getElementById('edit_id').value : '';
    const correoInput = document.getElementById('id_correo').value;

    // Validación de la matrícula
    try {
        const response = await fetch(`/validar-matricula-profesor/?matricula=${encodeURIComponent(matriculaInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Matrícula ya registrada");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "La matrícula ya está registrada";
            return false;
        }
    } catch (error) {
        console.error('Error al validar la matrícula:', error);
        alert("Ocurrió un error al validar la matrícula. Inténtalo de nuevo.");
        return false;
    }

    // Validación del correo
    try {
          // Asegúrate de que el campo correo esté en el HTML
        const response = await fetch(`/validar-correo-profesor/?correo=${encodeURIComponent(correoInput)}&id=${directivoId}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Correo ya registrado");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "El correo ya está registrado";
            return false;
        }
    } catch (error) {
        console.error('Error al validar el correo:', error);
        alert("Ocurrió un error al validar el correo. Inténtalo de nuevo.");
        return false;
    }

    event.target.submit();
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
    const inputBusqueda = document.getElementById('busqueda-profesor');
    const contenedorProfesores = document.getElementById('profesores-conainer');

    inputBusqueda.addEventListener('keyup', function () {
        const query = this.value;

        fetch(`/buscar-profesores/?q=${query}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            contenedorProfesores.innerHTML = '';  // Limpia los resultados anteriores

            // Añade los nuevos resultados dinámicamente
            data.forEach(profesor => {
                const item = document.createElement('div');
                item.className = 'grid-item';
                item.innerHTML = `
                    <h4>${profesor.nombre} ${profesor.apellidos}</h4>
                    <p><strong>Matrícula:</strong> ${profesor.matricula}</p>
                    <p><strong>Correo:</strong> ${profesor.correo}</p>
                    <p><strong>Contraseña:</strong> ${profesor.contrasena}</p>
                    <div class="grid-actions">
                        <a href="/GestionHorarios/${profesor.id}" class="update-btn">Ver Horarios</a>
                        <a href="/EliminarProfesor/${profesor.id}" class="delete-btn" onclick="return confirm('¿Estás seguro de que deseas eliminar a este profesor?')">Eliminar</a>
                        <button class="update-btn" onclick="openModal(${profesor.id}, '${profesor.nombre}', '${profesor.apellidos}', '${profesor.matricula}', '${profesor.contrasena}', '${profesor.correo}')">Actualizar</button>
                    </div>
                `;
                contenedorProfesores.appendChild(item);
            });            
        });
    });
});