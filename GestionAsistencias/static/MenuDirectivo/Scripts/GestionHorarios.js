function openModal(id, lunes, martes, miercoles, jueves, viernes, idperi) {

    document.getElementById('editForm').action = `EditarHorario/${id}`;
    document.getElementById('lunes_id').value = lunes || '';
    document.getElementById('martes_id').value = martes || '';
    document.getElementById('miercoles_id').value = miercoles || '';
    document.getElementById('jueves_id').value = jueves || '';
    document.getElementById('viernes_id').value = viernes || '';
    document.getElementById('id_periodo_id').value = idperi;
    document.getElementById('edit_id').value = id;
    document.getElementById('editModal').style.display = 'flex';
}

async function validarCrear(event) {
    event.preventDefault();

    const periodoInput = document.getElementById('id_idPeriodo').value;
    const profesorId = document.getElementById('profesorId').value;
    const mensaje = document.getElementById('Mensaje');

    // Validación del periodo
    try {
        const response = await fetch(`/validar-periodo-profesor/?idPeriodo=${encodeURIComponent(periodoInput)}&profesorId=${profesorId}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Periodo ya registrado para este profesor");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "El periodo ya está registrado para este profesor";
            return false;
        }
    } catch (error) {
        console.error('Error al validar el periodo:', error);
        alert("Ocurrió un error al validar el periodo. Inténtalo de nuevo.");
        return false;
    }

    
    event.target.submit();
}

async function validareditar(event) {
    event.preventDefault();

    const periodoInput = document.getElementById('id_periodo_id').value;
    const id = document.getElementById('edit_id').value;
    const profesorId = document.getElementById('profesorId').value; 
    const mensaje = document.getElementById('Mensaje');

    // Validación del periodo
    try {
        const response = await fetch(`/validar-periodo-profesor/?idPeriodo=${encodeURIComponent(periodoInput)}&profesorId=${profesorId}&id=${id}`);
        const data = await response.json();

        if (data.existe) {
            console.log("Periodo ya registrado para este profesor");  // Debug
            modal.style.display = 'flex';
            mensaje.innerText = "El periodo ya está registrado para este profesor";
            return false;
        }
    } catch (error) {
        console.error('Error al validar el periodo:', error);
        alert("Ocurrió un error al validar el periodo. Inténtalo de nuevo.");
        return false;
    }

    
    event.target.submit();
}


function CrearPDF(idProf, idHor){
    document.getElementById('SubirPDF').style.display = 'flex';
    document.getElementById('formSPDF').action = `/CrearPDF/${idProf}/${idHor}`; 
}

function CerrarCPDF(){
    document.getElementById('SubirPDF').style.display = 'none'
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


function CerrarAlerta() {
    document.getElementById('Alerta').style.display = 'none';
}

function abrirhorario(event, id, id2) {
    var contenido = document.getElementById('horario-' + id); // Selecciona el contenedor por su ID
    var contenido2 = document.getElementById('pdf-' + id2); // Selecciona el contenedor del PDF

    if (contenido) {
        contenido.style.display = "block"; // Muestra el contenedor del horario
    }

    if (contenido2) {
        contenido2.style.display = "none"; // Oculta el contenedor del PDF
    }
}

function abrirPDF(event, id, id2) {
    var contenido = document.getElementById('pdf-' + id); // Selecciona el contenedor del PDF
    var contenido2 = document.getElementById('horario-' + id2); // Selecciona el contenedor del horario

    // Oculta el contenedor del horario
    if (contenido2) {
        contenido2.style.display = "none"; // Ocultar el horario
    }

    // Muestra el contenedor del PDF
    if (contenido) {
        contenido.style.display = "block";
    }
}



function EditarPDF(idPDFhorario, nombre, idProfesor) {
    // Muestra el modal
    document.getElementById('Editarpdf').style.display = 'flex';

    // Configura la acción del formulario
    const form = document.getElementById('FormEdPDF');
    form.action = `/EditarPDF/${idPDFhorario}/${idProfesor}`;

    // Configura el campo del nombre
    document.getElementById('nombre_id').value = nombre;
}


function validarArchivoPDF(event) {
    event.preventDefault(); // Detenemos el envío del formulario

    // Obtenemos el archivo del input
    const inputArchivo = document.getElementById('id_horario_pdf');
    const archivo = inputArchivo.files[0];

    // Referencias para mostrar mensajes al usuario
    const modal = document.getElementById('Alerta'); // Modal o mensaje de alerta
    const mensaje = document.getElementById('Mensaje'); // Elemento donde mostrar el mensaje

    if (!archivo) {
        modal.style.display = 'flex';
        mensaje.innerText = "Por favor, selecciona un archivo.";
        return false;
    }

    // Validar extensión del archivo
    const nombreArchivo = archivo.name.toLowerCase();
    if (!nombreArchivo.endsWith('.pdf')) {
        modal.style.display = 'flex';
        mensaje.innerText = "El archivo debe tener la extensión .pdf.";
        return false;
    }

    // Validar tipo MIME del archivo
    if (archivo.type !== 'application/pdf') {
        modal.style.display = 'flex';
        mensaje.innerText = "El archivo debe ser un PDF válido.";
        return false;
    }

    // Si pasa las validaciones, se puede enviar el formulario
    event.target.submit();
}


function validarEditarPdf(event) {
    event.preventDefault(); // Detenemos el envío del formulario

    // Obtenemos el archivo del input
    const inputArchivo = document.getElementById('horario_pdf_id'); 
    const archivo = inputArchivo.files[0];

    // Referencias para mostrar mensajes al usuario
    const modal = document.getElementById('Alerta'); // Modal o mensaje de alerta
    const mensaje = document.getElementById('Mensaje'); // Elemento donde mostrar el mensaje

    if (!archivo) {
        modal.style.display = 'flex';
        mensaje.innerText = "Por favor, selecciona un archivo.";
        return false;
    }

    // Validar extensión del archivo
    const nombreArchivo = archivo.name.toLowerCase();
    if (!nombreArchivo.endsWith('.pdf')) {
        modal.style.display = 'flex';
        mensaje.innerText = "El archivo debe tener la extensión .pdf.";
        return false;
    }

    // Validar tipo MIME del archivo
    if (archivo.type !== 'application/pdf') {
        modal.style.display = 'flex';
        mensaje.innerText = "El archivo debe ser un PDF válido.";
        return false;
    }

    // Si pasa las validaciones, se puede enviar el formulario
    event.target.submit();
}