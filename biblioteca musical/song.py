from artist import Artist
from disc import Disc


class Song:
    '''
    Representa a una cancion perteneciente a un artista musical y un disco
    si estos se conocen.
    '''

    def __init__(self, connection, song_id=None, title=None, content=None, duration=None, type=None, artist=None, disc=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = song_id
        self.__title = title
        self.__content = content
        self.__duration = duration
        self.__type = type
        self.__artist = artist
        self.__disc = disc


    def __str__(self):
        result = f'La cancion con id {self.__id}, titulo = {self.__title}'
        if self.__artist is not None:
            result += '\n' + self.__artist.__str__()
        
        if self.__disc is not None:
            result += '\n' + self.__disc.__str__()
            
        return result
            
    
    def setDuration(self, duracion):
        self.__duration = duracion
    
    
    def reload(self):
        '''
        Carga en memoria una canción de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT Cancion.titulo, duracion, genero, contenido, id_artista, id_disco, '
        sql += 'nombre, nacionalidad, fecha_nacimiento, '
        sql += 'Disco.titulo, fecha, editor '
        sql += 'FROM Cancion '
        sql += 'JOIN Artista ON Artista.id = Cancion.id_artista ' 
        sql += 'JOIN Disco ON Disco.id = Cancion.id_disco '
        sql += 'WHERE titulo = ?'
        self.__cursor.execute(sql, (self.__title,))
        row = self.__cursor.fetchone()
        self.__title = row[0]    # Investigar cómo utilizar claves textuales
        self.__duration = row[1]
        self.__type = row[2]
        self.__content = row[3]
        self.__artist = Artist(self.__connection, row[4], row[6], row[7], row[8])
        self.__disc = Disc(self.__connection, row[5], row[9], row[10], row[11])
    


    def save(self):
        '''
        Añade una nueva canción a la base de datos.
        '''
        sql = 'INSERT INTO Cancion (id, titulo, contenido, duracion, genero, id_artista, id_disco) '
        sql += 'VALUES (?, ?, ?, ?, ?, ?, ?)'
        disc_id = self.__disc.getId() if self.__disc.getId() is not None else None
        artist_id = self.__artist.getId() if self.__artist.getId() is not None else None

        values = (
            self.__id,
            self.__title,
            self.__content,
            self.__duration,
            self.__type,
            artist_id,
            disc_id,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra una cancion existente en la base de datos.
        '''
        sql = 'DELETE FROM Cancion WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de una cancion existente en la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'UPDATE Cancion SET titulo = ?, contenido = ?, duracion = ?, genero = ?, id_artista = ?, id_disco = ?  '
        sql += 'WHERE id = ?'
        disc_id = self.__disc.getId() if self.__disc.getId() is not None else None
        artist_id = self.__artist.getId() if self.__artist.getId() is not None else None
        values = (
            self.__title,
            self.__content,
            self.__duration,
            self.__type,
            artist_id,
            disc_id,
            self.__id,

        )
        print(values)
        print(sql)
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    

    def load(self):
        '''
        Carga en memoria una canción de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT Cancion.titulo, duracion, genero, contenido, id_artista, id_disco, '
        sql += 'nombre, nacionalidad, fecha_nacimiento, '
        sql += 'Disco.titulo, fecha, editor '
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON Artista.id = Cancion.id_artista ' 
        sql += 'LEFT JOIN Disco ON Disco.id = Cancion.id_disco '
        sql += 'WHERE Cancion.id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
#         print(row)
        self.__title = row[0]    # Investigar cómo utilizar claves textuales
        self.__duration = row[1]
        self.__type = row[2]
        self.__content = row[3]
        if row[4] is not None: 
            self.__artist = Artist(self.__connection, row[4], row[6], row[7], row[8])
        if row[5] is not None:
            self.__disc = Disc(self.__connection, row[5], row[9], row[10], row[11])
    
