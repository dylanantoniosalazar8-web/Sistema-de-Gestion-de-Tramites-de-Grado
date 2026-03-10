CREATE DATABASE neondb;

CREATE OR REPLACE FUNCTION update_field_ts()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;



CREATE TABLE facultad (
    id_facultad SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_update_facultad
BEFORE UPDATE ON facultad
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE programa (
    id_programa SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_facultad INT NOT NULL,
    FOREIGN KEY (id_facultad) REFERENCES facultad(id_facultad),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_update_programa
BEFORE UPDATE ON programa
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE tipo_grado (
    id_tipo_grado SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_update_tipo_grado
BEFORE UPDATE ON tipo_grado
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE tipo_documento (
    id_tipo_documento SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_update_tipo_documento
BEFORE UPDATE ON tipo_documento
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    documento VARCHAR(30) NOT NULL UNIQUE,
    id_tipo_documento INT NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    id_programa INT NOT NULL,
    id_tipo_grado INT NOT NULL,
    fecha_nacimiento DATE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_programa) REFERENCES programa(id_programa),
    FOREIGN KEY (id_tipo_documento) REFERENCES tipo_documento(id_tipo_documento),
    FOREIGN KEY (id_tipo_grado) REFERENCES tipo_grado(id_tipo_grado)
);

CREATE TRIGGER trg_update_estudiante
BEFORE UPDATE ON estudiante
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE ceremonia_grado (
    id_ceremonia_grado SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha DATE NOT NULL,
    lugar VARCHAR(100),
    horario TIME,
    capacidad INT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_ceremonia_grado
BEFORE UPDATE ON ceremonia_grado
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE asignacion_ceremonia (
    id_asignacion_ceremonia SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_ceremonia_grado INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_ceremonia_grado) REFERENCES ceremonia_grado(id_ceremonia_grado),
    UNIQUE(id_estudiante, id_ceremonia_grado)
);

CREATE TRIGGER trg_asignacion_ceremonia
BEFORE UPDATE ON asignacion_ceremonia
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE documento_requerido (
    id_documento_requerido SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_tipo_grado INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_tipo_grado) REFERENCES tipo_grado(id_tipo_grado)
);

CREATE TRIGGER trg_documento_requerido
BEFORE UPDATE ON documento_requerido
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE entrega_documento (
    id_entrega_documento SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_documento_requerido INT NOT NULL,
    fecha_entrega DATE,
    estado VARCHAR(50) DEFAULT 'Pendiente',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_documento_requerido) REFERENCES documento_requerido(id_documento_requerido),
    UNIQUE(id_estudiante, id_documento_requerido)
);

CREATE TRIGGER trg_entrega_documento
BEFORE UPDATE ON entrega_documento
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE pago_tramite (
    id_pago_tramite SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATE NOT NULL,
    metodo_pago VARCHAR(50),
    estado VARCHAR(50) DEFAULT 'Pendiente', 
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TRIGGER trg_pago_tramite
BEFORE UPDATE ON pago_tramite
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE tipo_paz_ysalvo (
    id_tipo_paz_ysalvo SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

CREATE TRIGGER trg_tipo_paz_ysalvo
BEFORE UPDATE ON tipo_paz_ysalvo
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

CREATE TABLE paz_ysalvo (
    id_paz_ysalvo SERIAL PRIMARY KEY,
    id_tipo_paz_ysalvo INT NOT NULL,
    id_estudiante INT NOT NULL,
    fecha_aprobacion DATE ,
    estado VARCHAR(50) DEFAULT 'Pendiente',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_tipo_paz_ysalvo) REFERENCES tipo_paz_ysalvo(id_tipo_paz_ysalvo)
);

CREATE TRIGGER trg_paz_ysalvo
BEFORE UPDATE ON paz_ysalvo
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();


CREATE TABLE tramite_grado (
    id_tramite_grado SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_tipo_grado INT NOT NULL,
    fecha_inicio DATE DEFAULT CURRENT_DATE,
    fecha_fin DATE,
    estado VARCHAR(50) DEFAULT 'En Proceso',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    deleted_at TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_tipo_grado) REFERENCES tipo_grado(id_tipo_grado)
);

CREATE TRIGGER trg_tramite_grado
BEFORE UPDATE ON tramite_grado
FOR EACH ROW
EXECUTE FUNCTION update_field_ts();

