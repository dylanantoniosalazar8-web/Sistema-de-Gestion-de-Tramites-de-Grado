import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.sustentacion_model import Sustentacion
from fastapi.encoders import jsonable_encoder


class SustentacionController:

    def create_sustentacion(self, sustentacion: Sustentacion):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO sustentaciones
                (tramite_id, jurado_id, fecha, nota)
                VALUES (%s, %s, %s, %s)""",
                (sustentacion.tramite_id, sustentacion.jurado_id,
                 sustentacion.fecha, sustentacion.nota)
            )
            conn.commit()
            return {"resultado": "Sustentación creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_sustentacion(self, sustentacion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sustentaciones WHERE id = %s", (sustentacion_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            if result:
                content = {
                    'id': int(result[0]),
                    'tramite_id': result[1],
                    'jurado_id': result[2],
                    'fecha': result[3],
                    'nota': float(result[4]) if result[4] is not None else None
                }
                payload.append(content)
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Sustentación no encontrada")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_sustentaciones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sustentaciones")
            result = cursor.fetchall()
            payload = []
            content = {}

            for data in result:
                content = {
                    'id': data[0],
                    'tramite_id': data[1],
                    'jurado_id': data[2],
                    'fecha': data[3],
                    'nota': float(data[4]) if data[4] is not None else None
                }
                payload.append(content)
                content = {}

            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay sustentaciones")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_sustentacion(self, sustentacion_id: int, sustentacion: Sustentacion):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE sustentaciones
                SET tramite_id=%s, jurado_id=%s, fecha=%s, nota=%s
                WHERE id=%s""",
                (sustentacion.tramite_id, sustentacion.jurado_id,
                 sustentacion.fecha, sustentacion.nota, sustentacion_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Sustentación no encontrada")

            return {"resultado": "Sustentación actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_sustentacion(self, sustentacion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM sustentaciones WHERE id=%s",
                (sustentacion_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Sustentación no encontrada")

            return {"resultado": "Sustentación eliminada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()