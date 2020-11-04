import mysql.connector
import hashlib
bd = mysql.connector.connect(user ='chema', password = '12345', database = 'cinemapp')
cursor = bd.cursor()

def get_usuario():
    consulta = "SELECT * FROM usuario"
    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {'id': row[0], 'correo':row[1], 'usuario': row[2]}
        usuarios.append(usuario)
    return usuarios

def existe_usuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

def crear_usuario(correo,contra):
    if existe_usuario(correo):
        return False
    else:
        h = hashlib.new('sha256', bytes(contra, 'utf-8'))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario(correo, password) VALUES(%s, %s)"
        cursor.execute(insertar, (correo, h))
        bd.commit()
        return True

def iniciar_sesion(correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND password = %s"
    cursor.execute(query, (correo, h))
    id = cursor.fetchone()
    if id:
        return id[0], True
    else:
        return None, False
