import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.facultad_model import Facultad
from fastapi.encoders import jsonable_encoder


class FacultadController:

    def create_facultad(self, facultad: Facultad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO facultades (nombre) VALUES (%s)",
                (facultad.nombre,)
            )
            conn.commit()
            return {"resultado": "Facultad creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_facultad(self, facultad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM facultades WHERE id = %s",
                (facultad_id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            content = {
                "id": result[0],
                "nombre": result[1]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_facultades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay facultades")

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "nombre": data[1]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_facultad(self, facultad_id: int, facultad: Facultad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE facultades SET nombre=%s WHERE id=%s",
                (facultad.nombre, facultad_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            return {"resultado": "Facultad actualizada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_facultad(self, facultad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM facultades WHERE id=%s",
                (facultad_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            return {"resultado": "Facultad eliminada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()