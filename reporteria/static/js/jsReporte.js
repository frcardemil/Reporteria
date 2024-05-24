document.addEventListener('DOMContentLoaded', function () {
    newReport();
});

function newReport() {
    let reporte = document.getElementById('reporteRt');
    let razon = document.getElementById('razonRt');
    document.getElementById('btnSubmit').addEventListener('click', function () {
        if (reporte.files.length != 0) {
            if (reporte.files[0].name.slice(-5) == '.xlsx') {
                if (razon.innerText.length < 60) {
                    document.getElementById('formReportRt').submit();
                }
            }
        }
    });
};
function modificar(idReporte) {
    document.getElementById("u-idRt").value = document.getElementById("idRt-" + idReporte).innerText
    document.getElementById("u-razonRt").value = document.getElementById("razonRt-" + idReporte).innerText
    let id_areaRt = document.getElementById("id_areaRt-" + idReporte).innerText
    document.getElementById("u-id_areaRt").value = JSON.parse(id_areaRt)
    let fecha_json = document.getElementById("fecha_DatosRt-" + idReporte).innerText
    fecha_json = transformarDateEnDate(fecha_json)
    document.getElementById("u-fecha_DatosRt").value = fecha_json

    let razon = document.getElementById('u-razonRt');
    document.getElementById('u-btnSubmit').addEventListener('click', function () {
        if (razon.value.length < 60) {
            alert(razon.value.length)
            document.getElementById('u-formReportRt').submit();
        }
    });
}

function transformarDateEnDate(date) {
    var fecha = new Date(date);

    let dia = fecha.getDate();
    let mes = fecha.getMonth() + 1; // El mes comienza desde 0
    let anio = fecha.getFullYear();

    dia = dia < 10 ? '0' + dia : dia;
    mes = mes < 10 ? '0' + mes : mes;

    // Formatear la fecha en el formato "DD-MM-YYYY"
    let fechaFormateada = anio+'-'+mes+'-'+ dia ;
    return fechaFormateada
}
function limpiarForm(nameForm) {
    let reporteF = document.getElementById(nameForm)
    reporteF.reset();
}