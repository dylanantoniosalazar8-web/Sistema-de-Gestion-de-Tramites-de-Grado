import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_documento_model import TipoDocumento
from fastapi.encoders import jsonable_encoder


class TipoDocumentoController:

    def create_tipo_documento(self, data: TipoDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO tipo_documento (nombre)
                VALUES (%s)""",
                (data.nombre,)
            )

            conn.commit()
            return {"resultado": "Tipo de documento creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_tipo_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_documento,
                nombre
                FROM tipo_documento
                WHERE id_tipo_documento=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            content = {
                "id_tipo_documento": result[0],
                "nombre": result[1]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_tipos_documento(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tipo_documento,
                nombre
                FROM tipo_documento"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_tipo_documento": data[0],
                    "nombre": data[1]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay tipos de documento")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_tipo_documento(self, id: int, data: TipoDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE tipo_documento
                SET nombre=%s
                WHERE id_tipo_documento=%s""",
                (data.nombre, id)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            return {"resultado": "Tipo de documento actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_tipo_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM tipo_documento WHERE id_tipo_documento=%s",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            return {"resultado": "Tipo de documento eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()

            