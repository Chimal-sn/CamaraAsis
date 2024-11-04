const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const resultado = document.getElementById('resultado');

// Acceder a la cámara
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error al acceder a la cámara: ", err);
    });

// Función para capturar imagen y enviarla al servidor
function capturarYEnviar() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL('image/jpeg'); // Imagen en formato base64
    
    // Enviar la imagen capturada al servidor
    fetch('/compare_faces/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',  // Asegúrate de incluir el token CSRF
        },
        body: JSON.stringify({ imageData: dataURL })
    })
    .then(response => response.json())
    .then(data => {
        const modal = document.getElementById('editModal');
        const closeBtn = document.querySelector('.close');
        const registradoText = document.getElementById('Registrado');
        
        if (data.match) {
            resultado.textContent = `Bienvenido ${data.profesor_id}`;
            
            if (data.asistencia){
                modal.style.display = 'flex';
                Registrado.textContent ="Asistencia  registrada";

            // Cerrar modal automáticamente después de 3 segundosJ
                setTimeout(() => {
                    modal.style.display = 'none';
                }, 4000); // 3000 ms = 3 segundos
            }

        } else {
            resultado.textContent = 'No hay coincidencia de rostro.';
        }
    })
    .catch(error => {
        console.error('Error al comparar rostros:', error);
    });
}

// Captura y envía la imagen cada 5 segundos (o el intervalo que desees)
setInterval(capturarYEnviar, 5000);  // 5000 ms = 5 segundos
