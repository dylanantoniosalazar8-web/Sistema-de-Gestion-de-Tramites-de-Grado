import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tramite_grado_model import TramiteGrado
from fastapi.encoders import jsonable_encoder


class TramiteGradoController:

    def create_tramite_grado(self, data: TramiteGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO tramite_grado
                (id_estudiante, id_tipo_grado, fecha_inicio, fecha_fin, estado)
                VALUES (%s,%s,%s,%s,%s)""",
                (
                    data.id_estudiante,
                    data.id_tipo_grado,
                    data.fecha_inicio,
                    data.fecha_fin,
                    data.estado
                )
            )

            conn.commit()
            return {"resultado": "Trámite de grado registrado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al registrar el trámite")

        finally:
            conn.close()


    def get_tramite_grado(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tramite_grado,
                id_estudiante,
                id_tipo_grado,
                fecha_inicio,
                fecha_fin,
                estado
                FROM tramite_grado
                WHERE id_tramite_grado=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            content = {
                "id_tramite_grado": result[0],
                "id_estudiante": result[1],
                "id_tipo_grado": result[2],
                "fecha_inicio": result[3],
                "fecha_fin": result[4],
                "estado": result[5]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_tramites_grado(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_tramite_grado,
                id_estudiante,
                id_tipo_grado,
                fecha_inicio,
                fecha_fin,
                estado
                FROM tramite_grado"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_tramite_grado": data[0],
                    "id_estudiante": data[1],
                    "id_tipo_grado": data[2],
                    "fecha_inicio": data[3],
                    "fecha_fin": data[4],
                    "estado": data[5]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay trámites de grado registrados")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al obtener los trámites")

        finally:
            conn.close()


    def update_tramite_grado(self, id: int, data: TramiteGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE tramite_grado
                SET id_estudiante=%s,
                    id_tipo_grado=%s,
                    fecha_inicio=%s,
                    fecha_fin=%s,
                    estado=%s
                WHERE id_tramite_grado=%s""",
                (
                    data.id_estudiante,
                    data.id_tipo_grado,
                    data.fecha_inicio,
                    data.fecha_fin,
                    data.estado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            return {"resultado": "Trámite de grado actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar el trámite")

        finally:
            conn.close()


    def delete_tramite_grado(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM tramite_grado
                WHERE id_tramite_grado=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            return {"resultado": "Trámite de grado eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar el trámite")

        finally:
            conn.close()