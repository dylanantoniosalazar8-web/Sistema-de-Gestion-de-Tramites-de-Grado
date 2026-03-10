const usuario = JSON.parse(localStorage.getItem("usuario"))
if (!usuario || usuario.rol !== "admin") window.location = "index.html"

document.getElementById("bienvenida").textContent = "Bienvenido, " + usuario.nombre

function logout() {
  localStorage.removeItem("usuario")
  window.location = "index.html"
}


let tramites = []

async function cargarTramites() {
  let res = await fetch("http://localhost:8000/get_tramites_grado/")
  const data = await res.json()
  tramites = data.resultado
  renderTramites(tramites)
}

function renderTramites(data) {
  let html = "<table border='1'>"
  html += "<tr><th>ID</th><th>Estudiante</th><th>Tipo Grado</th><th>Fecha Inicio</th><th>Estado</th><th>Acciones</th></tr>"
  data.forEach(t => {
    html += `<tr>
      <td>${t.id_tramite_grado}</td>
      <td>${t.id_estudiante}</td>
      <td>${t.id_tipo_grado}</td>
      <td>${t.fecha_inicio || "—"}</td>
      <td>${t.estado}</td>
      <td>
        <button onclick="editarTramite(${t.id_tramite_grado})">Editar</button>
        <button onclick="eliminarTramite(${t.id_tramite_grado})">Eliminar</button>
      </td>
    </tr>`
  })
  html += "</table>"
  document.getElementById("tabla").innerHTML = html
}

function abrirFormNuevo() {
  document.getElementById("formNuevo").style.display = "block"
}

function cerrarForm() {
  document.getElementById("formNuevo").style.display = "none"
}

async function crearTramite() {
  const body = {
    id_estudiante: parseInt(document.getElementById("nuevoEstudiante").value),
    id_tipo_grado: parseInt(document.getElementById("nuevoTipoGrado").value),
    fecha_inicio: document.getElementById("nuevoFecha").value || null,
    estado: document.getElementById("nuevoEstado").value
  }
  await fetch("http://localhost:8000/create_tramite_grado", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  })
  cerrarForm()
  cargarTramites()
}

async function editarTramite(id) {
  const t = tramites.find(x => x.id_tramite_grado === id)
  const nuevoEstado = prompt("Nuevo estado:", t.estado)
  if (!nuevoEstado) return
  await fetch("http://localhost:8000/update_tramite_grado/" + id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ...t, estado: nuevoEstado })
  })
  cargarTramites()
}

async function eliminarTramite(id) {
  if (!confirm("¿Eliminar trámite #" + id + "?")) return
  await fetch("http://localhost:8000/delete_tramite_grado/" + id, { method: "DELETE" })
  cargarTramites()
}


cargarTramites()