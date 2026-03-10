import psycopg2
from models.entrega_documento_model import EntregaDocumento
from config.db_config import get_db_connection
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


class EntregaDocumentoController:

    def create_entrega_documento(self, data: EntregaDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO entrega_documento
                (id_estudiante, id_documento_requerido, fecha_entrega, estado)
                VALUES (%s,%s,%s,%s)""",
                (
                    data.id_estudiante,
                    data.id_documento_requerido,
                    data.fecha_entrega,
                    data.estado
                )
            )

            conn.commit()
            return {"resultado": "Entrega de documento registrada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_entrega_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_entrega_documento,
                id_estudiante,
                id_documento_requerido,
                fecha_entrega,
                estado
                FROM entrega_documento
                WHERE id_entrega_documento=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Entrega no encontrada")

            content = {
                "id_entrega_documento": result[0],
                "id_estudiante": result[1],
                "id_documento_requerido": result[2],
                "fecha_entrega": result[3],
                "estado": result[4]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_entregas_documentos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_entrega_documento,
                id_estudiante,
                id_documento_requerido,
                fecha_entrega,
                estado
                FROM entrega_documento"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_entrega_documento": data[0],
                    "id_estudiante": data[1],
                    "id_documento_requerido": data[2],
                    "fecha_entrega": data[3],
                    "estado": data[4]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay entregas registradas")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_entrega_documento(self, id: int, data: EntregaDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE entrega_documento
                SET id_estudiante=%s,
                    id_documento_requerido=%s,
                    fecha_entrega=%s,
                    estado=%s
                WHERE id_entrega_documento=%s""",
                (
                    data.id_estudiante,
                    data.id_documento_requerido,
                    data.fecha_entrega,
                    data.estado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Entrega no encontrada")

            return {"resultado": "Entrega actualizada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_entrega_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM entrega_documento
                WHERE id_entrega_documento=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Entrega no encontrada")

            return {"resultado": "Entrega eliminada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()