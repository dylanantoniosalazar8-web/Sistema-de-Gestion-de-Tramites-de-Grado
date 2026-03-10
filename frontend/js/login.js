async function login(){

let correo = document.getElementById("correo").value
let password = document.getElementById("password").value

let res = await fetch("http://localhost:3000/usuarios")

let usuarios = await res.json()

let usuario = usuarios.find(u => u.correo === correo && u.password === password)

if(usuario){

localStorage.setItem("usuario", JSON.stringify(usuario))

window.location = "dashboard.html"

}else{

alert("Usuario incorrecto")

}

}