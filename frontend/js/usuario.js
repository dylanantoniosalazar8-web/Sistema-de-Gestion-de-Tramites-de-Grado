async function verUsuarios(){

let res = await fetch("http://localhost:3000/usuarios")

let usuarios = await res.json()

let html = "<table border='1'>"

html += "<tr><th>ID</th><th>Nombre</th><th>Correo</th></tr>"

usuarios.forEach(u => {

html += `
<tr>
<td>${u.id_usuario}</td>
<td>${u.nombre}</td>
<td>${u.correo}</td>
</tr>
`

})

html += "</table>"

document.getElementById("tabla").innerHTML = html

}