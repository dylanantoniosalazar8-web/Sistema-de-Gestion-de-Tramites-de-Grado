import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tramitegrado_model import TramiteGrado
from fastapi.encoders import jsonable_encoder


class TramiteGradoController:

    def create_tramite(self, tramite: TramiteGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO tramites_grado
                (estudiante_id, estado, observaciones)
                VALUES (%s, %s, %s)""",
                (tramite.estudiante_id, tramite.estado, tramite.observaciones)
            )
            conn.commit()
            return {"resultado": "Trámite creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_tramite(self, tramite_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tramites_grado WHERE id=%s",
                (tramite_id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Trámite no encontrado")

            content = {
                "id": result[0],
                "estudiante_id": result[1],
                "fecha_solicitud": result[2],
                "estado": result[3],
                "observaciones": result[4]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_tramites(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tramites_grado")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay trámites")

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "estudiante_id": data[1],
                    "fecha_solicitud": data[2],
                    "estado": data[3],
                    "observaciones": data[4]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_tramite(self, tramite_id: int, tramite: TramiteGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE tramites_grado
                SET estudiante_id=%s, estado=%s, observaciones=%s
                WHERE id=%s""",
                (tramite.estudiante_id, tramite.estado,
                 tramite.observaciones, tramite_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Trámite no encontrado")

            return {"resultado": "Trámite actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_tramite(self, tramite_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM tramites_grado WHERE id=%s",
                (tramite_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Trámite no encontrado")

            return {"resultado": "Trámite eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()