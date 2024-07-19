document.addEventListener('DOMContentLoaded', function () {
    addGrafico("myChart-");
});

let meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

function addGrafico(nameID) {
    fetch('/reporteria/api/reporte/')
        .then(response => response.json())
        .then(data => {
            let propiedades = [['entrega_a_tiempo', 'entrega_total'], ['pedido_proveedor', 'stock_productos'],
            ['venta_realizada', 'venta_pedido'], ['factura_pagada', 'factura_total'],['boleta_pagada', 'boleta_total']];
            let nameLabels = [['Entregas a tiempo', 'Total Entregas'], ['Stock Proveedores', 'Stock Empresa'],
            ['Ventas completadas', 'Ventas solicitadas'], ['Facturas Pagadas', 'Total Facturas'],['Boletas Pagadas', 'Total Boletas']];
            let listaData = [];
            let nombreLabel = [];
            for (let index = 0; index < data.length; index++) {
                let listaDataRt = [];
                const reporte = data[index];
                console.log(reporte);
                let fecha = reporte.anno_mes_rt / 100;
                fecha = fecha.toString().split('.');
                for (let i in propiedades) {
                    listaDataRt.push(addDatos(reporte, propiedades[i][0], propiedades[i][1], fecha, listaData[i], 0));
                }
                listaData = listaDataRt
            }
            for (let i = 0; i < propiedades.length; i++) {
                nombreLabel = [nameLabels[i][0], nameLabels[i][1]];
                editarGrafico(nameID + i, listaData[i], meses, nombreLabel);
            }
        })
        .catch((error) => {
            console.error('GET Error:', error);
        });
}

function addDatos(data, propiedad1, propiedad2, fecha, listaDataRt, index) {
    let listaDataTmp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
    if (listaDataRt) {
        listaDataTmp = listaDataRt;
    }
    for (let i = 0; i < meses.length; i++) {
        const mes = meses[i];
        if (meses[fecha[1] - 1] == mes) {
            listaDataTmp[0][i] = data[propiedad1]
            listaDataTmp[1][i] = data[propiedad2]
        }
    }
    return listaDataTmp;
}
function editarGrafico(nameID, listaData, listaNameData, nombreLabel) {
    // Obtener el contexto del canvas
    const ctx = document.getElementById(nameID).getContext('2d');
    // Crear el gráfico con Chart.js
    const miGrafico = new Chart(ctx, {
        type: 'line', // Cambia a 'line' para un gráfico de líneas, etc.
        data: {
            labels: listaNameData,
            datasets: [{
                label: nombreLabel[0],
                data: listaData[0],
                backgroundColor: '#32E0C4', // Color de fondo de las barras
                borderColor: '#32E0C4', // Color del borde de las barras
                borderWidth: 1
            },
            {
                label: nombreLabel[1],
                data: listaData[1],
                backgroundColor: '#222831', // Color de fondo de las barras
                borderColor: '#222831', // Color del borde de las barras
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Meses'
                    }
                },
                y: {
                    beginAtZero: true,
                    suggestedMax: 10,
                    title: {
                        display: true,
                        text: 'Cantidad'
                    }
                }
            },
            transitions: {
                show: {
                    animations: {
                        x: {
                            from: 0
                        },
                        y: {
                            from: 0
                        }
                    }
                },
                hide: {
                    animations: {
                        x: {
                            to: 0
                        },
                        y: {
                            to: 0
                        }
                    }
                }
            }
        }
    });
}