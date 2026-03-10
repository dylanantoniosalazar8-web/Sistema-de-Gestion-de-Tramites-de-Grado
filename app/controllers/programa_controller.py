import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.programa_model import Programa
from fastapi.encoders import jsonable_encoder


class ProgramaController:

    def create_programa(self, data: Programa):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO programa (nombre, id_facultad)
                VALUES (%s,%s)""",
                (data.nombre, data.id_facultad)
            )

            conn.commit()
            return {"resultado": "Programa creado"}

        finally:
            conn.close()

    def get_programa(self, id: int):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM programa WHERE id_programa=%s",
            (id,)
        )

        result = cursor.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Programa no encontrado")

        content = {
            "id_programa": result[0],
            "nombre": result[1],
            "id_facultad": result[2]
        }

        conn.close()
        return jsonable_encoder(content)

    def get_programas(self):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM programa")
        result = cursor.fetchall()

        payload = []

        for data in result:
            content = {
                "id_programa": data[0],
                "nombre": data[1],
                "id_facultad": data[2]
            }

            payload.append(content)

        conn.close()

        if result:
            return {"resultado": jsonable_encoder(payload)}
        else:
            raise HTTPException(status_code=404, detail="No hay programas")

    def update_programa(self, id: int, data: Programa):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE programa
            SET nombre=%s, id_facultad=%s
            WHERE id_programa=%s""",
            (data.nombre, data.id_facultad, id)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Programa no encontrado")

        conn.close()

        return {"resultado": "Programa actualizado"}

    def delete_programa(self, id: int):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM programa WHERE id_programa=%s",
            (id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Programa no encontrado")

        conn.close()

        return {"resultado": "Programa eliminado"}