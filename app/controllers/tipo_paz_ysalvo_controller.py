import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_paz_ysalvo_model import TipoPazYSalvo
from fastapi.encoders import jsonable_encoder


class TipoPazYSalvoController:

    def create_tipo_paz_ysalvo(self, data: TipoPazYSalvo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO tipo_paz_ysalvo
                (nombre)
                VALUES (%s)""",
                (data.nombre,)
            )

            conn.commit()
            return {"resultado": "Tipo de paz y salvo creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_tipo_paz_ysalvo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_paz_ysalvo,
                nombre
                FROM tipo_paz_ysalvo
                WHERE id_tipo_paz_ysalvo=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Tipo de paz y salvo no encontrado")

            content = {
                "id_tipo_paz_ysalvo": result[0],
                "nombre": result[1]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_tipos_paz_ysalvo(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_paz_ysalvo,
                nombre
                FROM tipo_paz_ysalvo"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_tipo_paz_ysalvo": data[0],
                    "nombre": data[1]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay tipos de paz y salvo")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_tipo_paz_ysalvo(self, id: int, data: TipoPazYSalvo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE tipo_paz_ysalvo
                SET nombre=%s
                WHERE id_tipo_paz_ysalvo=%s""",
                (
                    data.nombre,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de paz y salvo no encontrado")

            return {"resultado": "Tipo de paz y salvo actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_tipo_paz_ysalvo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM tipo_paz_ysalvo
                WHERE id_tipo_paz_ysalvo=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de paz y salvo no encontrado")

            return {"resultado": "Tipo de paz y salvo eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()