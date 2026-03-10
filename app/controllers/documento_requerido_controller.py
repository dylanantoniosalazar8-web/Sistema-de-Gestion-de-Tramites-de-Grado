import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.documento_requerido_model import DocumentoRequerido
from fastapi.encoders import jsonable_encoder


class DocumentoRequeridoController:

    def create_documento_requerido(self, data: DocumentoRequerido):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO documento_requerido
                (nombre, descripcion, id_tipo_grado)
                VALUES (%s,%s,%s)""",
                (
                    data.nombre,
                    data.descripcion,
                    data.id_tipo_grado
                )
            )

            conn.commit()
            return {"resultado": "Documento requerido creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_documento_requerido(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_documento_requerido,
                nombre,
                descripcion,
                id_tipo_grado
                FROM documento_requerido
                WHERE id_documento_requerido=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Documento requerido no encontrado")

            content = {
                "id_documento_requerido": result[0],
                "nombre": result[1],
                "descripcion": result[2],
                "id_tipo_grado": result[3]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_documentos_requeridos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_documento_requerido,
                nombre,
                descripcion,
                id_tipo_grado
                FROM documento_requerido"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_documento_requerido": data[0],
                    "nombre": data[1],
                    "descripcion": data[2],
                    "id_tipo_grado": data[3]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay documentos requeridos")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_documento_requerido(self, id: int, data: DocumentoRequerido):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE documento_requerido
                SET nombre=%s,
                    descripcion=%s,
                    id_tipo_grado=%s
                WHERE id_documento_requerido=%s""",
                (
                    data.nombre,
                    data.descripcion,
                    data.id_tipo_grado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Documento requerido no encontrado")

            return {"resultado": "Documento requerido actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_documento_requerido(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM documento_requerido
                WHERE id_documento_requerido=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Documento requerido no encontrado")

            return {"resultado": "Documento requerido eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()