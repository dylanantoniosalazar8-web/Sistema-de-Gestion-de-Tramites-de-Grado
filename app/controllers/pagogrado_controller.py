import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.pagogrado_model import PagoGrado
from fastapi.encoders import jsonable_encoder


class PagoGradoController:

    def create_pago(self, pago: PagoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO pagos_grado
                (tramite_id, valor, fecha_pago, estado)
                VALUES (%s, %s, %s, %s)""",
                (pago.tramite_id, pago.valor,
                 pago.fecha_pago, pago.estado)
            )
            conn.commit()
            return {"resultado": "Pago registrado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_pago(self, pago_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pagos_grado WHERE id = %s", (pago_id,))
            result = cursor.fetchone()
            payload = []
            content = {}

            if result:
                content = {
                    'id': int(result[0]),
                    'tramite_id': result[1],
                    'valor': float(result[2]),
                    'fecha_pago': result[3],
                    'estado': result[4]
                }
                payload.append(content)
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Pago no encontrado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_pagos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pagos_grado")
            result = cursor.fetchall()
            payload = []
            content = {}

            for data in result:
                content = {
                    'id': data[0],
                    'tramite_id': data[1],
                    'valor': float(data[2]),
                    'fecha_pago': data[3],
                    'estado': data[4]
                }
                payload.append(content)
                content = {}

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

    def update_pago(self, pago_id: int, pago: PagoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE pagos_grado SET tramite_id=%s, valor=%s, fecha_pago=%s, estado=%s WHERE id=%s",
                (pago.tramite_id, pago.valor, pago.fecha_pago, pago.estado, pago_id)
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

    def delete_pago(self, pago_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM pagos_grado WHERE id=%s",
                (pago_id,)
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