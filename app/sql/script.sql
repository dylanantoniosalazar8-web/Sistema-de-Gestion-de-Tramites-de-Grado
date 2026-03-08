-- Crear base de datos
CREATE DATABASE prueba;


-- Crear tabla

CREATE TABLE facultades (
   id SERIAL PRIMARY KEY,
   nombre VARCHAR(100) NOT NULL
);

CREATE TABLE programas (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  facultad_id INT REFERENCES facultades(id)
);

CREATE TABLE estudiantes (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  documento VARCHAR(20) UNIQUE NOT NULL,
  correo VARCHAR(100) UNIQUE NOT NULL,
  telefono VARCHAR(20),
  programa_id INT REFERENCES programas(id)
);

CREATE TABLE tramites_grado (
  id SERIAL PRIMARY KEY,
  estudiante_id INT REFERENCES estudiantes(id),
  fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  estado VARCHAR(20) DEFAULT 'pendiente',
  observaciones TEXT
);

CREATE TABLE requisitos_grado (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  descripcion TEXT
);

CREATE TABLE tramite_requisitos (
  id SERIAL PRIMARY KEY,
  tramite_id INT REFERENCES tramites_grado(id),
  requisito_id INT REFERENCES requisitos_grado(id),
  cumplido BOOLEAN DEFAULT FALSE
);

CREATE TABLE documentos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  obligatorio BOOLEAN DEFAULT TRUE
);

CREATE TABLE estudiante_documentos (
  id SERIAL PRIMARY KEY,
  estudiante_id INT REFERENCES estudiantes(id),
  documento_id INT REFERENCES documentos(id),
  entregado BOOLEAN DEFAULT FALSE,
  fecha_entrega TIMESTAMP
);

CREATE TABLE pagos_grado (
  id SERIAL PRIMARY KEY,
  tramite_id INT REFERENCES tramites_grado(id),
  valor NUMERIC(10,2),
  fecha_pago TIMESTAMP,
  estado VARCHAR(20)
);

CREATE TABLE jurados (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(100),
  especialidad VARCHAR(100)
);

CREATE TABLE sustentaciones (
  id SERIAL PRIMARY KEY,
  tramite_id INT REFERENCES tramites_grado(id),
  jurado_id INT REFERENCES jurados(id),
  fecha TIMESTAMP,
  nota NUMERIC(3,2)
);

-- Insertar registro
INSERT INTO usuarios (nombre, apellido, cedula, edad, usuario, contrasena)
VALUES ('pedro', 'perez', '10102020', 30, 'pperez', '12345');