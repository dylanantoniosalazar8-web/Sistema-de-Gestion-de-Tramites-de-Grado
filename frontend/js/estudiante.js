const usuario = JSON.parse(localStorage.getItem("usuario"))
if (!usuario || usuario.rol !== "estudiante") window.location = "index.html"

document.getElementById("bienvenida").textContent = "Bienvenido, " + usuario.nombre

function logout() {
  localStorage.removeItem("usuario")
  window.location = "index.html"
}


document.getElementById("infoEstudiante").innerHTML = `
  <table border="1">
    <tr><th>Nombre</th><td>${usuario.nombre}</td></tr>
    <tr><th>Documento</th><td>${usuario.documento}</td></tr>
    <tr><th>Correo</th><td>${usuario.correo}</td></tr>
    <tr><th>Programa</th><td>ID: ${usuario.id_programa}</td></tr>
  </table>
`


async function cargarTramite() {
  try {
    const res = await fetch("http://localhost:8000/get_tramites_grado/")
    const data = await res.json()
    const tramites = data.resultado || data
    const misTramites = tramites.filter(t => t.id_estudiante === usuario.id_estudiante)

    if (!misTramites.length) {
      document.getElementById("estadoTramite").innerHTML = "<p>No tienes trámites registrados aún.</p>"
      return
    }

    const t = misTramites[misTramites.length - 1]
    const colores = { "En Proceso": "#f59e0b", "Aprobado": "#10b981", "Rechazado": "#ef4444", "Finalizado": "#10b981" }
    const color = colores[t.estado] || "#6b7280"

    document.getElementById("estadoTramite").innerHTML = `
      <table border="1">
        <tr><th>ID Trámite</th><td>#${t.id_tramite_grado}</td></tr>
        <tr><th>Tipo Grado</th><td>ID: ${t.id_tipo_grado}</td></tr>
        <tr><th>Fecha Inicio</th><td>${t.fecha_inicio || "—"}</td></tr>
        <tr><th>Fecha Fin</th><td>${t.fecha_fin || "—"}</td></tr>
        <tr><th>Estado</th><td><strong style="color:${color}">${t.estado}</strong></td></tr>
      </table>
    `
  } catch(e) {
    document.getElementById("estadoTramite").innerHTML = "<p>Error cargando trámite.</p>"
  }
}


async function cargarPazSalvo() {
  try {
    const res = await fetch("http://localhost:8000/get_pazes_ysalvo/")
    const data = await res.json()
    const lista = data.resultado || data
    const misPaz = lista.filter(p => p.id_estudiante === usuario.id_estudiante)

    if (!misPaz.length) {
      document.getElementById("pazSalvo").innerHTML = "<p>No tienes paz y salvos registrados.</p>"
      return
    }

    const colores = { "Aprobado": "#10b981", "Pendiente": "#f59e0b", "Rechazado": "#ef4444" }
    let html = "<table border='1'><tr><th>ID</th><th>Tipo</th><th>Fecha Aprobación</th><th>Estado</th></tr>"
    misPaz.forEach(p => {
      const color = colores[p.estado] || "#6b7280"
      html += `<tr>
        <td>#${p.id_paz_ysalvo}</td>
        <td>ID: ${p.id_tipo_paz_ysalvo}</td>
        <td>${p.fecha_aprobacion || "—"}</td>
        <td><strong style="color:${color}">${p.estado}</strong></td>
      </tr>`
    })
    html += "</table>"
    document.getElementById("pazSalvo").innerHTML = html
  } catch(e) {
    document.getElementById("pazSalvo").innerHTML = "<p>Error cargando paz y salvo.</p>"
  }
}


async function verificarAplica() {
  try {
    const res = await fetch("http://localhost:8000/verificar_aplica_grado/" + usuario.id_estudiante)
    const data = await res.json()
    const icon = data.aplica_grado ? "✅" : ""
    const color = data.aplica_grado ? "#10b981" : "#f59e0b"
    document.getElementById("aplicaGrado").innerHTML = `
      <p style="font-size:1.1rem;color:${color}">
        <strong>${icon} ${data.aplica_grado ? "Sí puedes aplicar a grado" : "Aún no puedes aplicar a grado"}</strong>
      </p>
      <p style="color:#6b7280;margin-top:8px">${data.mensaje || ""}</p>
    `
  } catch(e) {
    document.getElementById("aplicaGrado").innerHTML = "<p>Error verificando estado.</p>"
  }
}


cargarTramite()
cargarPazSalvo()
verificarAplica()
