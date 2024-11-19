function abrirCrear() {
    const modal = document.getElementById('ModalReporte');
    modal.style.display = 'flex'; // Muestra el modal
}

function cerrarModal() {
    const modal = document.getElementById('ModalReporte');
    modal.style.display = 'none'; // Oculta el modal
}

function generarReporte(tipo) {
    const form = document.getElementById('FormRepor');


    form.action = tipo;
    form.submit();
}

