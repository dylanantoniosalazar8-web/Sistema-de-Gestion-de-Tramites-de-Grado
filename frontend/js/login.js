const ADMIN = {
  correo: "admin@grado.edu",
  password: "admin123",
  rol: "admin",
  nombre: "Administrador"
}

async function login() {
  let correo = document.getElementById("correo").value.trim()
  let password = document.getElementById("password").value

  
  if (correo === ADMIN.correo && password === ADMIN.password) {
    localStorage.setItem("usuario", JSON.stringify(ADMIN))
    window.location = "dashboard_admin.html"
    return
  }

  
  try {
    let res = await fetch("http://localhost:8000/get_estudiantes/")
    const data = await res.json()
    let estudiantes = data.resultado || data
    let estudiante = estudiantes.find(e => e.correo === correo)

    if (estudiante && password === estudiante.documento) {
      localStorage.setItem("usuario", JSON.stringify({ ...estudiante, rol: "estudiante", nombre: estudiante.nombre + " " + estudiante.apellido }))
      window.location = "dashboard_estudiante.html"
    } else {
      alert("Correo o contraseña incorrectos")
    }
  } catch (e) {
    alert("Error conectando con el servidor. Verifica que la API esté activa.")
  }
}