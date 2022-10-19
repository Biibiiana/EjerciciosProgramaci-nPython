import sqlite3

from song import Song
from artist import Artist
from disc import Disc


class SongManager:
    '''Gestiona los objetos de la clase Song en la base de datos'''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    
    def __getSong(self, row):
        '''
        Crea un objeto Song a partir de un registro de la base de datos.

        row: registro de la base datos (con información de canción, artista, disco)
        Resultado: canción (Song)
        '''
        my_artist = None
        if row['id_artista'] is not None:
            my_artist = Artist(
                self.__connection,
                row['id_artista'],
                row['nombre'],
                row['nacionalidad'],
                row['fecha_nacimiento']
            )
        my_disc = None
        if row['id_disco'] is not None:
            my_disc = Disc(
                self.__connection,
                row['id_disco'],
                row['d_titulo'],
                row['fecha'],
                row['editor']
            )
        my_song = Song(
            self.__connection,
            row['c_id'],
            row['c_titulo'],
            row['contenido'],
            row['duracion'],
            row['genero'],
            my_artist,
            my_disc
        )
        return my_song


    def __getSongSet(self, rows):
        '''
        Crea una colección de canciones a partir de registros de la base de datos.

        rows: lista de registros de la base datos (con información de canción, artista, disco)
        Resultado: colección de canciones (set)
        '''
        result = set()
        if rows is None:
            return result
        for row in rows:
            my_song = self.__getSong(row)
            result.add(my_song)
        return result


    def getByIds(self, *ids):
        '''Obtiene las canciones correspondientes a los ids indicados.

        ids: colección de ids correspondientes a canciones en la base de datos
        resultado: (set) objetos de la clase Song
        '''

        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, genero, duracion, contenido, id_artista, id_disco, '    # canción
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor '  # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON (Artista.id = Cancion.id_artista) '
        sql += 'LEFT JOIN Disco ON (Disco.id = Cancion.id_disco) '
        sql += 'WHERE Cancion.id IN {}'.format(ids)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        return self.__getSongSet(rows)


    def getByTitle(self, title):
        '''Obtiene las canciones según el título indicado (o parte del mismo).

        title: título o parte de la canción (str)
        resultado: colección de canciones (set)
        '''
        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, genero, duracion, contenido, id_artista, id_disco, '    # canción
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor '  # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON (Artista.id = Cancion.id_artista) '
        sql += 'LEFT JOIN Disco ON (Disco.id = Cancion.id_disco) '
        sql += 'WHERE lower(c_titulo) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{title}%',))
        rows = self.__cursor.fetchall()
        return self.__getSongSet(rows)
