function submitLog() {
    buttonDisabled(true, 'btnSubmit');
    ocultarError();
    username = document.getElementsByName("ususarioLog")[0];
    password = document.getElementsByName("contrasenaLog")[0];
    if (!valLogin(username, password)) {
        event.preventDefault();
        buttonDisabled(false, 'btnSubmit');
    }
}
function valLogin(username, password) {
    estado = true;
    if (!(username.value.length >= 5 && username.value.length < 150)) {
        mostrarError(1);
        estaod = false;
    }
    if (!(password.value.length >= 6 && password.value.length < 150)) {
        mostrarError(2);
        estado = false;
    }
    return estado;
}

function verPassword() {
    password = document.getElementsByName("contrasenaLog")[0];
    iconEye = document.getElementById("eye-icon");
    if (password.getAttribute("type") == "text") {
        iconEye.classList.remove("fa-eye-slash");
        iconEye.classList.add("fa-eye");
        password.setAttribute("type", "password");
    }
    else if (password.getAttribute("type") == "password") {
        iconEye.classList.remove("fa-eye");
        iconEye.classList.add("fa-eye-slash");
        password.setAttribute("type", "text");
    }
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
function mostrarError(nro) {
    error = 'e';
    switch (nro) {
        case 1:
            document.getElementById(error + '-username').style.display = 'block';
            break;
        case 2:
            document.getElementById(error + '-password').style.display = 'block';
            break;
        default:
            break;
    }
}
function ocultarError() {
    document.getElementById('e-username').style.display = 'none';
    document.getElementById('e-password').style.display = 'none';
    if (document.getElementById('e-no-existe')) {
        document.getElementById('e-no-existe').style.display = 'none';
    }
}