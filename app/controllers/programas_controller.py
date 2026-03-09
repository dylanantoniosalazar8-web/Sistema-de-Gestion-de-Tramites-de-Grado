import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.programa_model import Programa
from fastapi.encoders import jsonable_encoder


class ProgramaController:

    def create_programa(self, programa: Programa):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO programas (nombre, facultad_id) VALUES (%s, %s)",
                (programa.nombre, programa.facultad_id)
            )
            conn.commit()
            return {"resultado": "Programa creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_programa(self, programa_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM programas WHERE id=%s",
                (programa_id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Programa no encontrado")

            content = {
                "id": result[0],
                "nombre": result[1],
                "facultad_id": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_programas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM programas")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay programas")

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "nombre": data[1],
                    "facultad_id": data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_programa(self, programa_id: int, programa: Programa):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE programas SET nombre=%s, facultad_id=%s WHERE id=%s",
                (programa.nombre, programa.facultad_id, programa_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Programa no encontrado")

            return {"resultado": "Programa actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_programa(self, programa_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM programas WHERE id=%s",
                (programa_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Programa no encontrado")

            return {"resultado": "Programa eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()