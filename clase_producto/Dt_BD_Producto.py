#CREAR BASE DE DATOS

import sqlite3

base_de_d="productos_bd.db"
#conectar a la base de datos de sqlite
def conectar(query,parameters=()):
    with sqlite3.connect(base_de_d)as conn:
        cursor=conn.cursor()
        resultados= cursor.execute(query,parameters)
        conn.commit()
    return resultados

#CREAR TABLA DE PRODUCTOS SI NO EXISTE
def crear_table():
    query=('''
                      CREATE TABLE IF NOT EXISTS productos(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     Producto TEXT unique NOT NULL,
                     Proovedor text not null,
                     Cantidad integer not null,
                     Descripcion tex not null
                    )
                   ''')
    conectar(query)
#insertar productos en la  base de datos
def insertar_Productos(producto,proovedor,cantidad,descripcion):
    query='insert into productos VALUES (NULL,?,?,?,?)'
    parameters=(producto,proovedor,cantidad,descripcion)
    conectar(query,parameters)
    

def obtener_productos():
    query= "SELECT * FROM productos ORDER BY producto DESC"
    db_row=conectar(query)
    return db_row

def eliminar_productos(producto):
    query='DELETE FROM productos where producto=?'
    conectar(query,(producto,))

def actualizar_productos(producto_nuevo,producto_actual,cantidad_nuevo,cantidad_actual):
    query='UPDATE productos set producto = ? , cantidad = ? where producto = ? and cantidad = ?'
    parameters=(producto_nuevo,cantidad_nuevo,producto_actual,cantidad_actual)
    conectar(query,parameters)


    
crear_table()
# insertar_Productos("camisas","estilo inico",50,"prendas informal") 
# insertar_Productos("short"," estilo unico",30,"algodon")
# insertar_Productos("camperas","estilo unico",50,"material resistente")
# insertar_Productos("zapatos","estilo unico",20,"bellisimas")
 


                                  

