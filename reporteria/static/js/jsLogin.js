function submitLog(){
    username = document.getElementsByName("ususarioLog")[0];
    password = document.getElementsByName("contrasenaLog")[0];
    if (!valLogin(username,password)){
        event.preventDefault();
    }
}
function valLogin(username,password){
    if (username.length >= 5 && password.length >=6) {
        return true
    } else {
        return false
    }
}