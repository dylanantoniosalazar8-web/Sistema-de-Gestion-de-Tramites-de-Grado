import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.facultad_model import Facultad
from fastapi.encoders import jsonable_encoder


class FacultadController:

    def create_facultad(self, data: Facultad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO facultad (nombre)
                VALUES (%s)""",
                (data.nombre,)
            )
            conn.commit()
            return {"resultado": "Facultad creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_facultad(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM facultad WHERE id_facultad=%s",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            content = {
                "id_facultad": result[0],
                "nombre": result[1]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()

    def get_facultades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultad")

            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    "id_facultad": data[0],
                    "nombre": data[1]
                }
                payload.append(content)

            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No hay facultades")

        finally:
            conn.close()

    def update_facultad(self, id: int, data: Facultad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE facultad
                SET nombre=%s
                WHERE id_facultad=%s""",
                (data.nombre, id)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            return {"resultado": "Facultad actualizada"}

        finally:
            conn.close()

    def delete_facultad(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM facultad WHERE id_facultad=%s",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            return {"resultado": "Facultad eliminada"}

        finally:
            conn.close()