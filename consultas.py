from peewee import *

# Conexión con la base de datos
db = MySQLDatabase(
    "biblioteca_universitaria",
    user="root",
    password="TU_CONTRASEÑA",
    host="localhost",
    port=3306
)

# Modelo base
class BaseModel(Model):
    class Meta:
        database = db


# Modelo de la tabla usuario
class Usuario(BaseModel):
    dni = CharField(primary_key=True)
    nombre = CharField()
    apellido = CharField()

    class Meta:
        table_name = "usuario"


# Modelo de la tabla ejemplar
class Ejemplar(BaseModel):
    codigo_de_inventario = IntegerField(primary_key=True)
    disponibilidad = CharField()
    libro_codigo_interno = IntegerField()

    class Meta:
        table_name = "ejemplar"


# Modelo de la tabla prestamo
class Prestamo(BaseModel):
    id_prestamo = AutoField()
    fecha_prestamo = DateField()
    fecha_devolucion = DateField(null=True)
    estado = CharField()

    dni = ForeignKeyField(
        Usuario,
        field=Usuario.dni,
        column_name="dni"
    )

    codigo_de_inventario = ForeignKeyField(
        Ejemplar,
        field=Ejemplar.codigo_de_inventario,
        column_name="codigo_de_inventario"
    )

    class Meta:
        table_name = "prestamo"


try:
    db.connect()

    # SELECT: consultar préstamos y sus usuarios
    consulta = Prestamo.select(Prestamo, Usuario).join(Usuario)

    print("Préstamos y usuarios:")

    for prestamo in consulta:
        print(
            "Préstamo:", prestamo.id_prestamo,
            "| Usuario:", prestamo.dni.nombre,
            prestamo.dni.apellido,
            "| Estado:", prestamo.estado
        )

        # INSERT: crear un préstamo de prueba (ya lo ejecutamos)
    # usuario_prueba = Usuario.get_by_id("30111222")
    # ejemplar_prueba = Ejemplar.get_by_id(1002)

    # nuevo_prestamo = Prestamo.create(
    #     fecha_prestamo="2026-10-17",
    #     fecha_devolucion=None,
    #     estado="Prueba",
    #     dni=usuario_prueba,
    #     codigo_de_inventario=ejemplar_prueba
    # )

    # print("Préstamo de prueba creado. ID:", nuevo_prestamo.id_prestamo)


    # UPDATE: cambiar el estado (ya lo ejecutamos)
    # Prestamo.update(
    #     estado="Devuelto"
    # ).where(
    #     Prestamo.id_prestamo == nuevo_prestamo.id_prestamo
    # ).execute()


    # DELETE: eliminar únicamente el préstamo de prueba ID 4
    Prestamo.delete().where(
        Prestamo.id_prestamo == 4
    ).execute()

    print("Préstamo de prueba ID 4 eliminado.")

finally:
    if not db.is_closed():
        db.close()