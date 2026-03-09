import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estudiante_model import Estudiante
from fastapi.encoders import jsonable_encoder


class EstudianteController:

    def create_estudiante(self, estudiante: Estudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO estudiantes 
                (nombre, documento, correo, telefono, programa_id) 
                VALUES (%s, %s, %s, %s, %s)""",
                (estudiante.nombre, estudiante.documento,
                 estudiante.correo, estudiante.telefono,
                 estudiante.programa_id)
            )
            conn.commit()
            return {"resultado": "Estudiante creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def get_estudiante(self, estudiante_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM estudiantes WHERE id_estudiante=%s",
                (estudiante_id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            content = {
                "id_estudiante": result[0],
                "nombre": result[1],
                "documento": result[2],
                "correo": result[3],
                "telefono": result[4],
                "programa_id": result[5]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def get_estudiantes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM estudiantes")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay estudiantes")

            payload = []

            for data in result:
                payload.append({
                    "id_estudiante": data[0],
                    "nombre": data[1],
                    "documento": data[2],
                    "correo": data[3],
                    "telefono": data[4],
                    "programa_id": data[5]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def update_estudiante(self, estudiante_id: int, estudiante: Estudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE estudiantes 
                SET nombre=%s, documento=%s, correo=%s, telefono=%s, programa_id=%s
                WHERE id_estudiante=%s""",
                (estudiante.nombre, estudiante.documento,
                 estudiante.correo, estudiante.telefono,
                 estudiante.programa_id, estudiante_id)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            return {"resultado": "Estudiante actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()


    def delete_estudiante(self, estudiante_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM estudiantes WHERE id_estudiante=%s",
                (estudiante_id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            return {"resultado": "Estudiante eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()