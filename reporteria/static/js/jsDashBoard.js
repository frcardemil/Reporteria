//
document.addEventListener('DOMContentLoaded', function() {
    let ids_reportes = document.getElementById('ipt-ids-reportes').value
    ids_reportes = JSON.parse(ids_reportes)
    for (let id_reporte of ids_reportes) {
        console.log(id_reporte)
        addGrafico("myChart-"+id_reporte, id_reporte);
    }
});

function addGrafico(nameID, id) {
    fetch('/reporteria/excelList/'+id+'/')
        .then(response => response.json())
        .then(data => {
            let nombreLabel = data[0][0] +' / ' + data[0][1]
            let listaNameData = []
            let listaData = []
            for (let i = 1; i < data.length; i++) {
                const element = data[i];
                listaNameData.push(element[0])
                listaData.push(element[1])
            }
            console.log(nombreLabel)
            console.log(listaNameData)
            console.log(listaData)
            editarGrafico(nameID,listaData, listaNameData, nombreLabel)
        })
        .catch((error) => {
            console.error('GET Error:', error);
        });

    // Ejemplo de solicitud POST
    const postData = {
        nombre: "John",
        edad: 30
    };

    
}
function editarGrafico(nameID,listaData, listaNameData, nombreLabel){
    // Obtener el contexto del canvas
    const ctx = document.getElementById(nameID).getContext('2d');
    // Crear el gráfico con Chart.js
    const miGrafico = new Chart(ctx, {
        type: 'line', // Cambia a 'line' para un gráfico de líneas, etc.
        data: {
            labels: listaNameData,
            datasets: [{
                label: nombreLabel,
                data: listaData,
                backgroundColor: '#32E0C4', // Color de fondo de las barras
                borderColor: '#32E0C4', // Color del borde de las barras
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}