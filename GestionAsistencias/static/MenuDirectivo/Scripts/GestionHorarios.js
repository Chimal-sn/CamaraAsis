function openModal(id, lunes, martes, miercoles, jueves, viernes, idperi) {
    console.log(`Valores: ${lunes}, ${martes}, ${miercoles}, ${jueves}, ${viernes}`); // Verifica los valores

    document.getElementById('editForm').action = `EditarHorario/${id}`;
    document.getElementById('id_Lunes').value = lunes || '';
    document.getElementById('id_Martes').value = martes || '';
    document.getElementById('id_Miercoles').value = miercoles || '';
    document.getElementById('id_Jueves').value = jueves || '';
    document.getElementById('id_Viernes').value = viernes || '';
    document.getElementById('id_idPeriodo').value = idperi;
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