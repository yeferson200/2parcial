import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='usuarios',
    port=3306
)


def getAllUsers():
    cursor = DB.cursor(dictionary=True)

    cursor.execute('select * from usuarios')

    return cursor.fetchall()


def crearBase (hostl, usuario, contraseña, puerto, basedatos):
    cursor = DB.cursor(dictionary=True)

    cursor.execute('''
        INSERT INTO usuarios(host, usuario, contraseña, puerto, basedatos)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (hostl, usuario, contraseña, puerto, basedatos))

    DB.commit()
    cursor.close()