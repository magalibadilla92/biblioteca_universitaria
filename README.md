# Biblioteca Universitaria

Sistema de gestión de una biblioteca universitaria desarrollado como trabajo parcial 2 de Base de Datos.

## Descripción

El proyecto permite organizar información de usuarios, autores, libros, ejemplares y préstamos. La base de datos se implementó en MySQL y se realizaron consultas desde Python utilizando el ORM Peewee.

## Tecnologías utilizadas

- MySQL: creación y administración de la base de datos.
- Python: programación de consultas.
- Peewee: mapeo de tablas y operaciones sobre la base de datos.

## Estructura del repositorio

- `consultas.py`: código Python para realizar operaciones sobre la base de datos.
- `respaldo_biblioteca_universitaria.sql`: respaldo SQL de la base de datos.
- `README.md`: descripción del proyecto.

## Configuración

Para ejecutar `consultas.py`, se necesita Python, MySQL y las bibliotecas `peewee` y `pymysql`.

Instalación de dependencias:

```bash
py -m pip install peewee pymysql
```

En `consultas.py`, configurá los datos de conexión a tu instancia de MySQL y asegurate de que exista la base de datos `biblioteca_universitaria`.

Configuración de conexión: Por seguridad, el archivo consultas.py contiene una contraseña de ejemplo. Para ejecutar el programa, se deben configurar las credenciales de MySQL correspondientes al entorno local. No se deben publicar contraseñas reales.

## Repositorio

[GitHub: biblioteca_universitaria](https://github.com/magalibadilla92/biblioteca_universitaria)

