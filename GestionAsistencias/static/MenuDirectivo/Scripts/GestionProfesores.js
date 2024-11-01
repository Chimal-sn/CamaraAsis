
function openModal(id, nombre, apellido, matricula, contrasena, correo) {
    document.getElementById('editForm').action = `/EditarProfesor/${id}`;
    document.getElementById('id_nombre').value = nombre;
    document.getElementById('id_apellido').value = apellido;
    document.getElementById('id_matricula').value = matricula;
    document.getElementById('id_Contrasena').value = contrasena;
    document.getElementById('id_Correo').value = correo;

    document.getElementById('editModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('editModal').style.display = 'none';
}

function validateMatricula() {
    const matriculaInput = document.getElementById('id_matricula').value;
    if (existingMatriculas.includes(matriculaInput)) {
        alert("Esta matrícula ya está registrada.");
        return false; // Evita el envío del formulario
    }
    return true; // Permite el envío del formulario
}



function abrirCrear(){
    document.getElementById('CrearModal').style.display = 'flex';
}

function CerrarModalCrear() {
    document.getElementById('CrearModal').style.display = 'none';
}