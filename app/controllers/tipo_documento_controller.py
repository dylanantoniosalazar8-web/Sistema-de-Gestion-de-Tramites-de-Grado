import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
<<<<<<< HEAD
from models.tramite_grado_model import TramiteGrado
from fastapi.encoders import jsonable_encoder


class TramiteGradoController:

    def create_tramite_grado(self, data: TramiteGrado):
=======
from models.tipo_documento_model import TipoDocumento
from fastapi.encoders import jsonable_encoder


class TipoDocumentoController:

    def create_tipo_documento(self, data: TipoDocumento):
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
<<<<<<< HEAD
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
=======
                """INSERT INTO tipo_documento (nombre)
                VALUES (%s)""",
                (data.nombre,)
            )

            conn.commit()
            return {"resultado": "Tipo de documento creado"}
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
<<<<<<< HEAD
            raise HTTPException(status_code=500, detail="Error al registrar el trámite")
=======
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        finally:
            conn.close()


<<<<<<< HEAD
    def get_tramite_grado(self, id: int):
=======
    def get_tipo_documento(self, id: int):
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
<<<<<<< HEAD
                id_tramite_grado,
                id_estudiante,
                id_tipo_grado,
                fecha_inicio,
                fecha_fin,
                estado
                FROM tramite_grado
                WHERE id_tramite_grado=%s""",
=======
                id_tipo_documento,
                nombre
                FROM tipo_documento
                WHERE id_tipo_documento=%s""",
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
                (id,)
            )

            result = cursor.fetchone()

            if not result:
<<<<<<< HEAD
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            content = {
                "id_tramite_grado": result[0],
                "id_estudiante": result[1],
                "id_tipo_grado": result[2],
                "fecha_inicio": result[3],
                "fecha_fin": result[4],
                "estado": result[5]
=======
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            content = {
                "id_tipo_documento": result[0],
                "nombre": result[1]
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
            }

            return jsonable_encoder(content)

        finally:
            conn.close()


<<<<<<< HEAD
    def get_tramites_grado(self):
=======
    def get_tipos_documento(self):
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                """SELECT
<<<<<<< HEAD
                id_tramite_grado,
                id_estudiante,
                id_tipo_grado,
                fecha_inicio,
                fecha_fin,
                estado
                FROM tramite_grado"""
=======
                id_tipo_documento,
                nombre
                FROM tipo_documento"""
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
            )

            result = cursor.fetchall()

            payload = []

            for data in result:
                content = {
<<<<<<< HEAD
                    "id_tramite_grado": data[0],
                    "id_estudiante": data[1],
                    "id_tipo_grado": data[2],
                    "fecha_inicio": data[3],
                    "fecha_fin": data[4],
                    "estado": data[5]
=======
                    "id_tipo_documento": data[0],
                    "nombre": data[1]
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
                }

                payload.append(content)

            json_data = jsonable_encoder(payload)

            if result:
                return {"resultado": json_data}
            else:
<<<<<<< HEAD
                raise HTTPException(status_code=404, detail="No hay trámites de grado registrados")
=======
                raise HTTPException(status_code=404, detail="No hay tipos de documento")
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
<<<<<<< HEAD
            raise HTTPException(status_code=500, detail="Error al obtener los trámites")
=======
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        finally:
            conn.close()


<<<<<<< HEAD
    def update_tramite_grado(self, id: int, data: TramiteGrado):
=======
    def update_tipo_documento(self, id: int, data: TipoDocumento):
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
<<<<<<< HEAD
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
=======
                """UPDATE tipo_documento
                SET nombre=%s
                WHERE id_tipo_documento=%s""",
                (data.nombre, id)
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
            )

            conn.commit()

            if cursor.rowcount == 0:
<<<<<<< HEAD
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            return {"resultado": "Trámite de grado actualizado"}
=======
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            return {"resultado": "Tipo de documento actualizado"}
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
<<<<<<< HEAD
            raise HTTPException(status_code=500, detail="Error al actualizar el trámite")
=======
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        finally:
            conn.close()


<<<<<<< HEAD
    def delete_tramite_grado(self, id: int):
=======
    def delete_tipo_documento(self, id: int):
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
<<<<<<< HEAD
                """DELETE FROM tramite_grado
                WHERE id_tramite_grado=%s""",
=======
                "DELETE FROM tipo_documento WHERE id_tipo_documento=%s",
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
<<<<<<< HEAD
                raise HTTPException(status_code=404, detail="Trámite de grado no encontrado")

            return {"resultado": "Trámite de grado eliminado"}
=======
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")

            return {"resultado": "Tipo de documento eliminado"}
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f

        except psycopg2.Error as err:
            print(err)
            conn.rollback()
<<<<<<< HEAD
            raise HTTPException(status_code=500, detail="Error al eliminar el trámite")

        finally:
            conn.close()
=======

        finally:
            conn.close()

            
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
