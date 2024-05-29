#CREAR BASE DE DATOS

import sqlite3

#conectar a la base de datos de sqlite
def conectar():
    conn= sqlite3.connect("productos_bd")
    return conn

#CREAR TABLA DE PRODUCTOS SI NO EXISTE
def crear_table():
    conn= conectar()
    cursor=conn.cursor()
    cursor.execute('''
                      CREATE TABLE IF NOT EXISTS productos(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     Producto TEXT unique NOT NULL,
                     Proovedor text not null,
                     Cantidad integer not null,
                     Descripcion tex not null
                    )
                   ''')
    

    conn.commit()
    conn.close()