// Selecciona el modal, el botón y el botón de cerrar
const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeModalBtn = document.querySelector('.close-btn');

// Abre el modal al hacer clic en el botón
openModalBtn.onclick = function() {
    modal.style.display = 'flex'; // Cambia de 'none' a 'flex' para mostrar el modal
}

// Cierra el modal al hacer clic en la 'x'
closeModalBtn.onclick = function() {
    modal.style.display = 'none';
}

// Cierra el modal al hacer clic fuera del contenido del modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
