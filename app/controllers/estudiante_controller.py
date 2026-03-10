import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estudiante_model import Estudiante
from fastapi.encoders import jsonable_encoder


class EstudianteController:

    def create_estudiante(self, data: Estudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO estudiante
                (nombre, apellido, documento, id_tipo_documento,
                correo, id_programa, id_tipo_grado, fecha_nacimiento)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (
                    data.nombre,
                    data.apellido,
                    data.documento,
                    data.id_tipo_documento,
                    data.correo,
                    data.id_programa,
                    data.id_tipo_grado,
                    data.fecha_nacimiento
                )
            )

            conn.commit()
            return {"resultado": "Estudiante creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_estudiante(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_estudiante,
                nombre,
                apellido,
                documento,
                id_tipo_documento,
                correo,
                id_programa,
                id_tipo_grado,
                fecha_nacimiento
                FROM estudiante
                WHERE id_estudiante=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            content = {
                "id_estudiante": result[0],
                "nombre": result[1],
                "apellido": result[2],
                "documento": result[3],
                "id_tipo_documento": result[4],
                "correo": result[5],
                "id_programa": result[6],
                "id_tipo_grado": result[7],
                "fecha_nacimiento": result[8]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_estudiantes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_estudiante,
                nombre,
                apellido,
                documento,
                id_tipo_documento,
                correo,
                id_programa,
                id_tipo_grado,
                fecha_nacimiento
                FROM estudiante"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_estudiante": data[0],
                    "nombre": data[1],
                    "apellido": data[2],
                    "documento": data[3],
                    "id_tipo_documento": data[4],
                    "correo": data[5],
                    "id_programa": data[6],
                    "id_tipo_grado": data[7],
                    "fecha_nacimiento": data[8]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay estudiantes")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_estudiante(self, id: int, data: Estudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE estudiante
                SET nombre=%s,
                    apellido=%s,
                    documento=%s,
                    id_tipo_documento=%s,
                    correo=%s,
                    id_programa=%s,
                    id_tipo_grado=%s,
                    fecha_nacimiento=%s
                WHERE id_estudiante=%s""",
                (
                    data.nombre,
                    data.apellido,
                    data.documento,
                    data.id_tipo_documento,
                    data.correo,
                    data.id_programa,
                    data.id_tipo_grado,
                    data.fecha_nacimiento,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            return {"resultado": "Estudiante actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_estudiante(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM estudiante WHERE id_estudiante=%s",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            return {"resultado": "Estudiante eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()

    def verificar_aplica_grado(self, id: int):

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

        
            cursor.execute("""
            SELECT COUNT(*)
            FROM pago_tramite
            WHERE id_estudiante = %s
            AND estado = 'Pagado'
            """, (id,))
        
            pago = cursor.fetchone()[0]

            if pago == 0:
                return {
                    "aplica_grado": False,
                    "mensaje": "El estudiante no ha pagado el trámite de grado"
            }

            
            cursor.execute("""
            SELECT COUNT(*)
            FROM documento_requerido dr
            LEFT JOIN entrega_documento ed
            ON dr.id_documento_requerido = ed.id_documento_requerido
            AND ed.id_estudiante = %s
            WHERE ed.estado != 'Aprobado' OR ed.estado IS NULL
            """, (id,))

            documentos_pendientes = cursor.fetchone()[0]

            if documentos_pendientes > 0:
                return {
                    "aplica_grado": False,
                    "mensaje": "El estudiante tiene documentos pendientes"
            }

          
            cursor.execute("""
            SELECT COUNT(*)
            FROM paz_ysalvo
            WHERE id_estudiante = %s
            AND estado != 'Aprobado'
             """, (id,))

            pazysalvo_pendiente = cursor.fetchone()[0]

            if pazysalvo_pendiente > 0:
                return {
                    "aplica_grado": False,
                    "mensaje": "El estudiante tiene paz y salvo pendientes"
            }

            return {
                "aplica_grado": True,
                "mensaje": "El estudiante cumple todos los requisitos para grado"
            }

        finally:
            conn.close()