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

def insertar_pelicula(pelicula):
    titulo = pelicula['titulo']
    fecha_visto = pelicula['fecha_visto']
    imagen = pelicula['imagen']
    director = pelicula['director']
    date = pelicula['date']
    usuarioId = pelicula['usuarioId']
    insertar = "INSERT INTO pelicula(titulo, fecha_visto, imagen, director, date, usuarioId) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(insertar,(titulo, fecha_visto, imagen, director, date, usuarioId))
    bd.commit()
    if cursor.rowcount:
        return True
    else:
        return False

def get_peliculas():
    query = "SELECT id, titulo, imagen, fecha_visto, director, date FROM pelicula"
    cursor.execute(query)
    peliculas = []
    for row in cursor.fetchall():
        pelicula = {
            'id': row[0],
            'titulo': row[1],
            'imagen': row[2],
            'fecha_visto': row[3],
            'director': row[4],
            'anio': row[5]    
        }
        peliculas.append(pelicula)
    return peliculas

def get_pelicula(id):
    query = "SELECT * FROM pelicula WHERE id = %s"
    cursor.execute(query, (id,))
    pelicula = {}
    row = cursor.fetchone()
    if row:
        pelicula['id'] = row[0]
        pelicula['titulo'] = row[1]
        pelicula['fecha_visto'] = row[2]
        pelicula['imagen'] = row[3]
        pelicula['director'] = row[4]
        pelicula['date'] = row[5]
        pelicula['valoracion'] = row[6]
        pelicula['favorito'] = row[7]
        pelicula['review'] = row[8]
        pelicula['compartido'] = row[9]
    return pelicula
