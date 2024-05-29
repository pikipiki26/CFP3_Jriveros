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
#insertar productos en la  base de datos
def insertar_Productos(producto,proovedor,cantidad,descripcion):
    conn=conectar()
    cursor=conn.cursor()
    cursor.execute('''
                   insert into productos (producto,proovedor,cantidad,descripcion)values
                 (?,?,?,?)
                 ''',(producto,proovedor,cantidad,descripcion))
    conn.commit()
    conn.close()

    
crear_table()
insertar_Productos("camisas","estilo inico",50,"prendas informal") 
# 
# 
# def run_query(query,parameters=()):
#     with sqlite3.connect(db_nombre) as conn:
#     cursor=    

# def obtener_producto():
#     query= SELECT * FROM  productos ORDER BY nombre DESC'


# def insertar_Productos(producto,proovedor,cantidad,descripcion):
#     query= INSERT INTO producto VALUES (NULL,?,?,?,?)
#     parameters=(producto,proovedor,cantidad,descripcion)
#     run_query(query,parameters)                                   

