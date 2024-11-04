function openModal(id, nombre, fechainicio, fechafin) {

    
    document.getElementById('editForm').action = `/EditarPeriodo/${id}`;
    document.getElementById('id_Nombre').value = nombre,
    document.getElementById('id_FechaInicio').value = fechainicio; 
    document.getElementById('id_FechaFin').value = fechafin;

    document.getElementById('editModal').style.display = 'flex';
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