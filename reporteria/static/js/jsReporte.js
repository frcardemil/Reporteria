document.addEventListener('DOMContentLoaded', function () {
    newReport();
})
function newReport() {
    reporte = document.getElementById('reporteRt');
    document.getElementById('btnSubmit').addEventListener('click', function () {
        if (reporte.files.length != 0) {
            if (reporte.files[0].name.slice(-5) == '.xlsx') {
                document.getElementById('formReportRt').submit();
            }
        }
    });
}
