document.addEventListener('DOMContentLoaded', function() {
    addGrafico("myChart-");
    console.log('xdxd');
});

let meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

function addGrafico(nameID) {
    fetch('/reporteria/api/reporte/')
        .then(response => response.json())
        .then(data => {
            let propiedades=[['entrega_a_tiempo','entrega_total'],['adquisicion_recibida','stock_productos'],
                            ['venta_realizada','venta_pedido'],['factura_pagada','factura_total']];
            let nameLabels=[['Entregas a tiempo','Total Entregas'],['Nuevo Stock','Total Stock'],
                            ['Ventas completadas','Ventas solicitadas'],['Facturas Pagadas','Total Facturas']];
            let listaData=[];
            let nombreLabel=[];
            for (let index = 0; index < data.length; index++) {
                let listaDataRt = [];
                const reporte = data[index];
                console.log(reporte);
                let fecha = reporte.mes_anno_reporte.split("-");
                for (let i in propiedades) {
                    listaDataRt.push(addDatos(reporte,propiedades[i][0],propiedades[i][1],fecha,listaData[i],0));
                }
                listaData=listaDataRt
                console.log(listaData[0]);
                console.log(index);
            }
            for (let i = 0; i < propiedades.length; i++) {
                nombreLabel=[nameLabels[i][0],nameLabels[i][1]];
                editarGrafico(nameID+i,listaData[i], meses, nombreLabel);
            }
        })
        .catch((error) => {
            console.error('GET Error:', error);
        });
}

function addDatos(data,propiedad1,propiedad2,fecha,listaDataRt,index){
    let listaDataTmp = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]];
    if (listaDataRt) {
        listaDataTmp=listaDataRt;
        console.log(listaDataTmp)
    }
    for (let i = 0; i < meses.length; i++) {
        const mes = meses[i];
        if (meses[fecha[1]-1]==mes){
            listaDataTmp[0][i]=data[propiedad1]
            listaDataTmp[1][i]=data[propiedad2]
        }
    }
    return listaDataTmp;
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
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}