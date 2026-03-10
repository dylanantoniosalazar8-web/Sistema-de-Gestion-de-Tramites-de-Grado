import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_grado_model import TipoGrado
from fastapi.encoders import jsonable_encoder


class TipoGradoController:

    def create_tipo_grado(self, data: TipoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO tipo_grado
                (nombre, descripcion)
                VALUES (%s,%s)""",
                (
                    data.nombre,
                    data.descripcion
                )
            )

            conn.commit()
            return {"resultado": "Tipo de grado creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_tipo_grado(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_grado,
                nombre,
                descripcion
                FROM tipo_grado
                WHERE id_tipo_grado=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            content = {
                "id_tipo_grado": result[0],
                "nombre": result[1],
                "descripcion": result[2]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_tipos_grado(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_grado,
                nombre,
                descripcion
                FROM tipo_grado"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_tipo_grado": data[0],
                    "nombre": data[1],
                    "descripcion": data[2]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay tipos de grado")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_tipo_grado(self, id: int, data: TipoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE tipo_grado
                SET nombre=%s,
                    descripcion=%s
                WHERE id_tipo_grado=%s""",
                (
                    data.nombre,
                    data.descripcion,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            return {"resultado": "Tipo de grado actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_tipo_grado(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM tipo_grado
                WHERE id_tipo_grado=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            return {"resultado": "Tipo de grado eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()