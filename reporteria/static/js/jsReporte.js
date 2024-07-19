document.addEventListener('DOMContentLoaded', function () {
    newReport();
});

function condicionSubmit() {
    let estado = false;
    let id_reporte = document.getElementById('newRt').value;
    
    if (id_reporte) {
        estado=true;
    } else {
        mostrarError(2);
    }
    return estado;
}

function newExcel(){
    const url = document.getElementById('url-excel').value;
    let id_Rt = document.getElementById('newRt').value;
    if (document.getElementById('newRt').value) {
        id_Rt = id_Rt.split('-');
        const href_URL = url.replace('pkRT', id_Rt[0]+id_Rt[1]);
        window.location.href = href_URL;
    } else {
        event.preventDefault();
    }
}
function newReport() {
    let btnID = 'btnSubmit';
    let formID = 'formReportRt';
    let btn = document.getElementById(btnID);

    let submitTmp = function () {
        buttonDisabled(true, btnID);
        if (condicionSubmit()) {
            document.getElementById(formID).submit();
            console.log('submit');
        }
        else {
            buttonDisabled(false, btnID);
            console.log('No submit');
        }
    }
    btn.addEventListener('click', submitTmp);
};

function limpiarForm(nameForm) {
    let reporteF = document.getElementById(nameForm)
    reporteF.reset();
}
function buttonDisabled(opcion, buttonID) {
    let button;
    //Añadir deshabilitar en el boton 'ButtonID'
    if (opcion == true) {
        button = document.getElementById(buttonID);
        button.classList.add('disabled');
    } else {
        //Remover deshabilitar en el boton 'ButtonID'
        button = document.getElementById(buttonID);
        button.classList.remove('disabled');
    }
}

function mostrarError(nro){
    error = 'e';
    switch (nro) {
        case 1:
            break;
        case 2:
            document.getElementById(error+'-mes_anno').style.display = 'block';
            console.log(document.getElementById(error+'-mes_anno'))
            break;
        default:
            break;
    }
}
function ocultarError(opcion){
    switch (opcion) {
        case 1:
            document.getElementById('e-rt').style.display = 'none';
            break;
        case 2:
            document.getElementById('e-mes_anno').style.display = 'none';
            break;
        default:
            break;
    }
}