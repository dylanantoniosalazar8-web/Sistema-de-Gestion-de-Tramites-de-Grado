import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.requisitogrado_model import RequisitoGrado
from fastapi.encoders import jsonable_encoder


class RequisitoGradoController:

    def create_requisito(self, requisito: RequisitoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO requisitos_grado (nombre, descripcion) VALUES (%s, %s)",
                (requisito.nombre, requisito.descripcion)
            )
            conn.commit()
            return {"resultado": "Requisito creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_requisito(self, requisito_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM requisitos_grado WHERE id=%s",
                (requisito_id,)
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Requisito no encontrado")

            content = {
                "id": result[0],
                "nombre": result[1],
                "descripcion": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_requisitos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM requisitos_grado")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay requisitos")

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "nombre": data[1],
                    "descripcion": data[2]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_requisito(self, requisito_id: int, requisito: RequisitoGrado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE requisitos_grado SET nombre=%s, descripcion=%s WHERE id=%s",
                (requisito.nombre, requisito.descripcion, requisito_id)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Requisito no encontrado")

            return {"resultado": "Requisito actualizado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_requisito(self, requisito_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM requisitos_grado WHERE id=%s",
                (requisito_id,)
            )
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Requisito no encontrado")

            return {"resultado": "Requisito eliminado"}

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()