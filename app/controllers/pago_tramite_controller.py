import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.pago_tramite_model import PagoTramite
from fastapi.encoders import jsonable_encoder


class PagoTramiteController:

    def create_pago_tramite(self, data: PagoTramite):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO pago_tramite
                (id_estudiante, monto, fecha_pago, metodo_pago, estado)
                VALUES (%s,%s,%s,%s,%s)""",
                (
                    data.id_estudiante,
                    data.monto,
                    data.fecha_pago,
                    data.metodo_pago,
                    data.estado
                )
            )

            conn.commit()
            return {"resultado": "Pago registrado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_pago_tramite(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_pago_tramite,
                id_estudiante,
                monto,
                fecha_pago,
                metodo_pago,
                estado
                FROM pago_tramite
                WHERE id_pago_tramite=%s""",
                (id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Pago no encontrado")

            content = {
                "id_pago_tramite": result[0],
                "id_estudiante": result[1],
                "monto": result[2],
                "fecha_pago": result[3],
                "metodo_pago": result[4],
                "estado": result[5]
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


    def get_pagos_tramite(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
                id_pago_tramite,
                id_estudiante,
                monto,
                fecha_pago,
                metodo_pago,
                estado
                FROM pago_tramite"""
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
                    "id_pago_tramite": data[0],
                    "id_estudiante": data[1],
                    "monto": data[2],
                    "fecha_pago": data[3],
                    "metodo_pago": data[4],
                    "estado": data[5]
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="No hay pagos registrados")

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_pago_tramite(self, id: int, data: PagoTramite):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE pago_tramite
                SET id_estudiante=%s,
                    monto=%s,
                    fecha_pago=%s,
                    metodo_pago=%s,
                    estado=%s
                WHERE id_pago_tramite=%s""",
                (
                    data.id_estudiante,
                    data.monto,
                    data.fecha_pago,
                    data.metodo_pago,
                    data.estado,
                    id
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Pago no encontrado")

            return {"resultado": "Pago actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_pago_tramite(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """DELETE FROM pago_tramite
                WHERE id_pago_tramite=%s""",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Pago no encontrado")

            return {"resultado": "Pago eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()