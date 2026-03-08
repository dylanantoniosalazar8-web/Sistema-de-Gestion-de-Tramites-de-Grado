import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estudiantedocumento_model import EstudianteDocumento
from fastapi.encoders import jsonable_encoder


class EstudianteDocumentoController:

    def create_estudiante_documento(self, data: EstudianteDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO estudiante_documentos
                (estudiante_id, documento_id, entregado, fecha_entrega)
                VALUES (%s, %s, %s, %s)""",
                (data.estudiante_id, data.documento_id,
                 data.entregado, data.fecha_entrega)
            )
            conn.commit()
            return {"resultado": "Documento asignado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_estudiante_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiante_documentos WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            if result:
                content = {
                    'id': int(result[0]),
                    'estudiante_id': result[1],
                    'documento_id': result[2],
                    'entregado': result[3],
                    'fecha_entrega': result[4]
                }
                payload.append(content)
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Registro no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_estudiante_documentos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiante_documentos")
            result = cursor.fetchall()
            payload = []
            content = {}

            for data in result:
                content = {
                    'id': data[0],
                    'estudiante_id': data[1],
                    'documento_id': data[2],
                    'entregado': data[3],
                    'fecha_entrega': data[4]
                }
                payload.append(content)
                content = {}

            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay registros")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_estudiante_documento(self, id: int, data: EstudianteDocumento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE estudiante_documentos
                SET estudiante_id=%s, documento_id=%s,
                entregado=%s, fecha_entrega=%s
                WHERE id=%s""",
                (data.estudiante_id, data.documento_id,
                 data.entregado, data.fecha_entrega, id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Registro no encontrado")

            return {"resultado": "Registro actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_estudiante_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM estudiante_documentos WHERE id=%s",
                (id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Registro no encontrado")

            return {"resultado": "Registro eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()