import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.jurado_model import Jurado
from fastapi.encoders import jsonable_encoder

class JuradoController:

    def create_jurado(self, jurado: Jurado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO jurados (nombre, correo, especialidad) VALUES (%s, %s, %s)",
                (jurado.nombre, jurado.correo, jurado.especialidad)
            )
            conn.commit()
            return {"resultado": "Jurado creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_jurado(self, jurado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM jurados WHERE id = %s", (jurado_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            if result:
                content = {
                    'id': int(result[0]),
                    'nombre': result[1],
                    'correo': result[2],
                    'especialidad': result[3]
                }
                payload.append(content)
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Jurado no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_jurados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM jurados")
            result = cursor.fetchall()
            payload = []
            content = {}

            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'correo': data[2],
                    'especialidad': data[3]
                }
                payload.append(content)
                content = {}

            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay jurados")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_jurado(self, jurado_id: int, jurado: Jurado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE jurados SET nombre=%s, correo=%s, especialidad=%s WHERE id=%s",
                (jurado.nombre, jurado.correo, jurado.especialidad, jurado_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Jurado no encontrado")

            return {"resultado": "Jurado actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_jurado(self, jurado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM jurados WHERE id = %s", (jurado_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Jurado no encontrado")

            return {"resultado": "Jurado eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()