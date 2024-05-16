function submitLog(){
    username = document.getElementsByName("ususarioLog")[0];
    password = document.getElementsByName("contrasenaLog")[0];
    if (!valLogin(username,password)){
        event.preventDefault();
    }
}
function valLogin(username,password){
    console.log(username.value)
    console.log(password.value)
    if (username.value.length >= 5 && password.value.length >=6) {
        console.log('true')
        return true
    } else {
        console.log('false')
        return false
    }
}