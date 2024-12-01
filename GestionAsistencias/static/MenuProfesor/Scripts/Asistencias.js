// Obtener todos los botones que abren el modal
const botonesAbrirModal = document.querySelectorAll('.abrir-modal');
const modal = document.getElementById('modal');
const spanCerrar = document.getElementsByClassName('close')[0];
const formulario = document.getElementById('justificacion-form');

// Agregar evento a cada botón
botonesAbrirModal.forEach(boton => {
    boton.addEventListener('click', function() {
        const asistenciaId = this.getAttribute('data-id');
        formulario.action = `/justificar/${asistenciaId}/`;
        modal.style.display = 'flex';  // Mostrar el modal
    });
});

// Cerrar el modal al hacer clic en la "X"
spanCerrar.onclick = function() {
    modal.style.display = 'none';
}

// Cerrar el modal si se hace clic fuera de él
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}