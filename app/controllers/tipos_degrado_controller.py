import psycopg2
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.models.tipos_degrado_model import TipoGrado
from config.db_config import get_db_connection


class TipoGradoController:

    def create_tipo_grado(self, tipo_grado: TipoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO tipo_grado
                (nombre, descripcion)
                VALUES (%s,%s)""",
                (tipo_grado.nombre, tipo_grado.descripcion)
            )

            conn.commit()
            return {"resultado": "Tipo de grado creado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_tipo_grado(self, id_tipo_grado: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM tipo_grado WHERE id_tipo_grado=%s",
                (id_tipo_grado,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            content = {
                "id_tipo_grado": result[0],
                "nombre": result[1],
                "descripcion": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def get_tipos_grado(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM tipo_grado")

            result = cursor.fetchall()

            payload = []

            for data in result:
                payload.append({
                    "id_tipo_grado": data[0],
                    "nombre": data[1],
                    "descripcion": data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def update_tipo_grado(self, id_tipo_grado: int, tipo_grado: TipoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE tipo_grado
                SET nombre=%s, descripcion=%s
                WHERE id_tipo_grado=%s""",
                (
                    tipo_grado.nombre,
                    tipo_grado.descripcion,
                    id_tipo_grado
                )
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            return {"resultado": "Tipo de grado actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()


    def delete_tipo_grado(self, id_tipo_grado: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM tipo_grado WHERE id_tipo_grado=%s",
                (id_tipo_grado,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo de grado no encontrado")

            return {"resultado": "Tipo de grado eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()

        finally:
            conn.close()