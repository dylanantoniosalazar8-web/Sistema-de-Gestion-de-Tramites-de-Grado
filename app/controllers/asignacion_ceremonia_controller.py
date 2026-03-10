import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asignacion_ceremonia_model import AsignacionCeremonia
from fastapi.encoders import jsonable_encoder


class AsignacionCeremoniaController:

    def create_asignacion_ceremonia(self, data: AsignacionCeremonia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO asignacion_ceremonia
                (id_estudiante, id_ceremonia_grado)
                VALUES (%s,%s)""",
                (
                    data.id_estudiante,
                    data.id_ceremonia_grado
                )
            )

            conn.commit()
            return {"resultado": "Asignación de ceremonia creada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_asignacion_ceremonia(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_asignacion_ceremonia,
                id_estudiante,
                id_ceremonia_grado
                FROM asignacion_ceremonia
                WHERE id_asignacion_ceremonia=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Asignación no encontrada")

            content = {
                "id_asignacion_ceremonia": result[0],
                "id_estudiante": result[1],
                "id_ceremonia_grado": result[2]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_asignaciones_ceremonia(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_asignacion_ceremonia,
                id_estudiante,
                id_ceremonia_grado
                FROM asignacion_ceremonia"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_asignacion_ceremonia": data[0],
                    "id_estudiante": data[1],
                    "id_ceremonia_grado": data[2]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay asignaciones")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_asignacion_ceremonia(self, id: int, data: AsignacionCeremonia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE asignacion_ceremonia
                SET id_estudiante=%s,
                    id_ceremonia_grado=%s
                WHERE id_asignacion_ceremonia=%s""",
                (
                    data.id_estudiante,
                    data.id_ceremonia_grado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Asignación no encontrada")

            return {"resultado": "Asignación actualizada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_asignacion_ceremonia(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM asignacion_ceremonia
                WHERE id_asignacion_ceremonia=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Asignación no encontrada")

            return {"resultado": "Asignación eliminada"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()