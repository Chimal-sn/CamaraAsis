document.addEventListener('DOMContentLoaded', function () {
    const inputBusqueda = document.getElementById('busqueda-periodo');
    const resultados = document.getElementById('resultados-busqueda');

    inputBusqueda.addEventListener('keyup', function () {
        const query = this.value;

        if (query.length > 0) {
            fetch(`/buscar-periodo/?q=${query}`, {
                method: 'GET',
            })
            .then(response => response.json())
            .then(data => {
                resultados.innerHTML = "";  // Limpia los resultados anteriores

                // Añade los nuevos resultados
                data.forEach(periodo => {
                    const li = document.createElement('li');
                    li.textContent = periodo.nombre;
                    li.dataset.id = periodo.id;
                    li.addEventListener('click', function () {
                        inputBusqueda.value = this.textContent; // Llena el input con el valor seleccionado
                        resultados.innerHTML = ""; // Limpia los resultados después de seleccionar
                    });
                    resultados.appendChild(li);
                });
            });
        } else {
            resultados.innerHTML = "";  // Limpia los resultados si no hay texto
        }
    });
});