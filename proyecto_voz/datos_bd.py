#Crear la base de datos

# import sqlite3

# # conectar a la base de datos de sqlite
# def conectar():
#     conn= sqlite3.connect("usuario.bd")
#     return conn

    
# #crear tabla de usuario si no exite.
# def crear_table():
#     conn= conectar()
#     cursor=conn.cursor()
#     cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS usuario(
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     usuario TEXT UNIQUE NOT NULL,
#                     contraseña text not null
#                     )
#                     ''')
#     conn.commit()
#     conn.close()


# #insertar usuario en la  base de datos
# def insertar_usuario(usuario,contraseña):
#     conn=conectar()
#     cursor=conn.cursor()
#     cursor.execute('''
#                  insert into usuario (usuario,contraseña)values
#                  (?,?)
#                  ''',(usuario,contraseña))
#     conn.commit()
#     conn.close()



# #VALIDAR USUARIO
# def validar_usuario(usuario,contraseña):
#     conn=conectar()
#     cursor=conn.cursor()
#     cursor.execute('''
#                   SELECT * FROM usuario WHERE usuario = ? AND  contraseña = ?
#     ''',(usuario,contraseña))

#     usuario_encontrado= cursor.fetchone()
#     conn.close()
#     return usuario_encontrado is not None


#crea tabla (ejecuta la funcion crear_tabla)
crear_table()
# insertar_usuario("JESI","2343")
# insertar_usuario("MAXI","2585JM")
# insertar_usuario("MILI","PIKI52")
#