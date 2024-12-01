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

function mostrarReporte(reporte) {
    // Ocultar ambos reportes
    document.getElementById('reporte-asistencias').style.display = 'none';
    document.getElementById('reporte-justificantes').style.display = 'none';

    // Mostrar el reporte seleccionado
    if (reporte === 'asistencias') {
        document.getElementById('reporte-asistencias').style.display = 'block';
    } else if (reporte === 'justificantes') {
        document.getElementById('reporte-justificantes').style.display = 'block';
    }
}