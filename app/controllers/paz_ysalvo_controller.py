import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.paz_ysalvo_model import PazYSalvo
from fastapi.encoders import jsonable_encoder


class PazYSalvoController:

    def create_paz_ysalvo(self, data: PazYSalvo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO paz_ysalvo
                (id_tipo_paz_ysalvo, id_estudiante, fecha_aprobacion, estado)
                VALUES (%s,%s,%s,%s)""",
                (
                    data.id_tipo_paz_ysalvo,
                    data.id_estudiante,
                    data.fecha_aprobacion,
                    data.estado
                )
            )

            conn.commit()
            return {"resultado": "Paz y salvo registrado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_paz_ysalvo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_paz_ysalvo,
                id_tipo_paz_ysalvo,
                id_estudiante,
                fecha_aprobacion,
                estado
                FROM paz_ysalvo
                WHERE id_paz_ysalvo=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Paz y salvo no encontrado")

            content = {
                "id_paz_ysalvo": result[0],
                "id_tipo_paz_ysalvo": result[1],
                "id_estudiante": result[2],
                "fecha_aprobacion": result[3],
                "estado": result[4]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_pazes_ysalvo(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_paz_ysalvo,
                id_tipo_paz_ysalvo,
                id_estudiante,
                fecha_aprobacion,
                estado
                FROM paz_ysalvo"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_paz_ysalvo": data[0],
                    "id_tipo_paz_ysalvo": data[1],
                    "id_estudiante": data[2],
                    "fecha_aprobacion": data[3],
                    "estado": data[4]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay paz y salvo registrados")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_paz_ysalvo(self, id: int, data: PazYSalvo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE paz_ysalvo
                SET id_tipo_paz_ysalvo=%s,
                    id_estudiante=%s,
                    fecha_aprobacion=%s,
                    estado=%s
                WHERE id_paz_ysalvo=%s""",
                (
                    data.id_tipo_paz_ysalvo,
                    data.id_estudiante,
                    data.fecha_aprobacion,
                    data.estado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Paz y salvo no encontrado")

            return {"resultado": "Paz y salvo actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_paz_ysalvo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM paz_ysalvo
                WHERE id_paz_ysalvo=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Paz y salvo no encontrado")

            return {"resultado": "Paz y salvo eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()