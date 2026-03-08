import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tramiterequisito_model import TramiteRequisito
from fastapi.encoders import jsonable_encoder


class TramiteRequisitoController:

    def create_tramite_requisito(self, data: TramiteRequisito):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO tramite_requisitos 
                (tramite_id, requisito_id, cumplido) 
                VALUES (%s, %s, %s)""",
                (data.tramite_id, data.requisito_id, data.cumplido)
            )
            conn.commit()
            return {"resultado": "Relación creada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_tramite_requisito(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tramite_requisitos WHERE id=%s",
                (id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Registro no encontrado")

            content = {
                "id": result[0],
                "tramite_id": result[1],
                "requisito_id": result[2],
                "cumplido": result[3]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_tramites_requisitos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tramite_requisitos")
            result = cursor.fetchall()
            payload = []
            content = {}

            for data in result:
                content = {
                    "id": data[0],
                    "tramite_id": data[1],
                    "requisito_id": data[2],
                    "cumplido": data[3]
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

    def update_tramite_requisito(self, id: int, data: TramiteRequisito):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE tramite_requisitos 
                SET tramite_id=%s, requisito_id=%s, cumplido=%s
                WHERE id=%s""",
                (data.tramite_id, data.requisito_id, data.cumplido, id)
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

    def delete_tramite_requisito(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tramite_requisitos WHERE id=%s",
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