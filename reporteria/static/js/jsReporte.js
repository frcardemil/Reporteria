document.addEventListener('DOMContentLoaded', function () {
    ocultarError();
    newReport();
});

function condicionSubmit(reporte, razon, fecha, update) {
    estado = false;
    cant = 0;
    function razonYfecha(razonTmp, fechaTmp) {
        let estadoTmp = false;
        let cantTmp = 0;
        if (razonTmp.value.length < 60 && razonTmp.value.length >= 1) {
            cantTmp+=1;
        } else {
            console.log('No hay razon');
            mostrarError(update,1)
        }
        if (fechaTmp.value) {
            cantTmp+=1;
        } else {
            console.log('No hay fecha');
            mostrarError(update,2)
        }
        if (cantTmp==2) {
            estadoTmp=true
        }
        return estadoTmp;
    }
    try {
        if (reporte.files.length != 0 || update) {
            cant+=1;
            if (reporte.files[0].name.slice(-5) == '.xlsx') {
                cant+=1;
            } else {
                console.log('No es un .xlsx');
                mostrarError(update,4)
            }
        } else {
            mostrarError(update,3);
            razonYfecha(razon, fecha);
        }
        if (cant==2 && razonYfecha(razon, fecha)) {
            estado=true;
        }
    } catch {
        if (update) {
            estado = razonYfecha(razon, fecha);
        }
    }
    return estado;
}


function submitForm(listaCondi, btnID, formID) {
    btn = document.getElementsByClassName(btnID)
    submitTmp = function () {
        ocultarError();
        buttonDisabled(true, btnID)
        if (condicionSubmit(listaCondi[0], listaCondi[1], listaCondi[2], listaCondi[3])) {
            document.getElementById(formID).submit();
            console.log('submit')
        }
        else {
            buttonDisabled(false, btnID);
            console.log('No submit')
        }
    }
    btn.addEventListener('click', submitTmp);
}

function newReport() {
    let reporte = document.getElementById('reporteRt');
    let razon = document.getElementById('razonRt');
    let fecha = document.getElementById('fecha_DatosRt');
    let listaCondi = [reporte, razon, fecha, false]
    submitForm(listaCondi, 'btnSubmit', 'formReportRt');
};

function modificar(idReporte) {
    btn = document.getElementById('u-btnSubmit')
    buttonDisabled(false, 'u-btnSubmit')
    try {
        btn.removeEventListener('click',submitTmp);
    } catch (error) {
        console.log('no existe el EventListener')
    }
    //ID
    document.getElementById("u-idRt").value = document.getElementById("idRt-" + idReporte).innerText;
    let idRt = document.getElementById("u-idRt");
    //RAZON
    document.getElementById("u-razonRt").value = document.getElementById("razonRt-" + idReporte).innerText;
    let razonRt = document.getElementById("u-razonRt");
    //AREA
    let id_areaRt = document.getElementById("id_areaRt-" + idReporte).innerText;
    document.getElementById("u-id_areaRt").value = JSON.parse(id_areaRt);
    id_areaRt = document.getElementById("u-id_areaRt");
    //FECHA_JSON
    let fecha_json = document.getElementById("fecha_DatosRt-" + idReporte).innerText;
    document.getElementById("u-fecha_DatosRt").value = transformarDateEnDate(fecha_json);
    fecha_json = document.getElementById("u-fecha_DatosRt");
    //REPORTE_FILE
    let reporteRt = document.getElementById('u-reporteRt');

    //SUBMIT
    let listaCondi = [reporteRt, razonRt, fecha_json, true];
    submitForm(listaCondi, 'u-btnSubmit', 'u-formReportRt');
}

function transformarDateEnDate(date) {
    var fecha = new Date(date);

    let dia = fecha.getDate();
    let mes = fecha.getMonth() + 1;
    let anio = fecha.getFullYear();

    dia = dia < 10 ? '0' + dia : dia;
    mes = mes < 10 ? '0' + mes : mes;

    let fechaFormateada = anio + '-' + mes + '-' + dia;
    return fechaFormateada
}
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

function mostrarError(update,nro){
    console.log(update)
    error = 'e';
    if (update) {
        error = 'eu'
    }
    switch (nro) {
        case 1:
            document.getElementById(error+'-razonRt').style.display = 'block';
            console.log(document.getElementById(error+'-razonRt'))
            break;
        case 2:
            document.getElementById(error+'-fecha_DatosRt').style.display = 'block';
            console.log(document.getElementById(error+'-fecha_DatosRt'))
            break;
        case 3:
            document.getElementById(error+'-reporteRt').innerText = 'Reporte no ha sido seleccionado'
            document.getElementById(error+'-reporteRt').style.display = 'block';
            console.log(document.getElementById(error+'-reporteRt'))
            break;
        case 4:
            document.getElementById(error+'-reporteRt').innerText = 'El archivo seleccionado no es .xlsx'
            document.getElementById(error+'-reporteRt').style.display = 'block';
            console.log(document.getElementById(error+'-reporteRt'))
            break;
        default:
            break;
    }
}
function ocultarError(){
    document.getElementById('e-razonRt').style.display = 'none';
    document.getElementById('e-fecha_DatosRt').style.display = 'none';
    document.getElementById('e-reporteRt').style.display = 'none';
    document.getElementById('eu-razonRt').style.display = 'none';
    document.getElementById('eu-fecha_DatosRt').style.display = 'none';
    document.getElementById('eu-reporteRt').style.display = 'none';
}