import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.documento_model import Documento
from fastapi.encoders import jsonable_encoder


class DocumentoController:

    def create_documento(self, documento: Documento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO documentos (nombre, obligatorio) VALUES (%s, %s)",
                (documento.nombre, documento.obligatorio)
            )
            conn.commit()
            return {"resultado": "Documento creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_documento(self, documento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM documentos WHERE id=%s",
                (documento_id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Documento no encontrado")

            content = {
                "id": result[0],
                "nombre": result[1],
                "obligatorio": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_documentos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documentos")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay documentos")

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "nombre": data[1],
                    "obligatorio": data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_documento(self, documento_id: int, documento: Documento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE documentos SET nombre=%s, obligatorio=%s WHERE id=%s",
                (documento.nombre, documento.obligatorio, documento_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Documento no encontrado")

            return {"resultado": "Documento actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_documento(self, documento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM documentos WHERE id=%s",
                (documento_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Documento no encontrado")

            return {"resultado": "Documento eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()