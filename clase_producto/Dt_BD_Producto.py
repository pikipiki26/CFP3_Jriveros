#CREAR BASE DE DATOS

import sqlite3

base_de_d="productos_bd.db"
#conectar a la base de datos de sqlite
def conectar():
    conn= sqlite3.connect(base_de_d)
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

    
# crear_table()
# insertar_Productos("camisas","estilo inico",50,"prendas informal") 
# insertar_Productos("short"," estilo unico",30,"algodon")
# insertar_Productos("camperas","estilo unico",50,"material resistente")
# insertar_Productos("zapatos","estilo unico",20,"bellisimas")
 

def obtener_productos():
    quary= "SELECT * FROM productos ORDER BY producto DESC"
    db_row=conectar(quary)
    return db_row

                                  

