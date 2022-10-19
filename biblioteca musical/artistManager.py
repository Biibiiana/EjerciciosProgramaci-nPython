from artist import Artist


class ArtistManager:
    '''Gestiona los objetos de la clase Artist en la base de datos'''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()

    
    def getByIds(self, *ids):
        '''devuelve una coleccion de objetos tipo artist
        ids = coleccion de ids correspondientes a artista
        resultado = devolvera un conjunto de objetos tipo Artist
        '''
        
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM artista '
        sql += 'WHERE id IN {} '.format(ids)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
            
        return result
    
    
    def getByName(self, name):
        '''devuelve una coleccion de objetos tipo artist segun su nombre
        name = contendrá parte del nombre de un artista (str)
        resultado = devolvera un conjunto de objetos tipo Artist
        '''
        
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM artista '
        sql += 'WHERE lower(nombre) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{name}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
            
        return result
    
    
    
    def getByNacionality(self, nacionality):
        '''devuelve una coleccion de objetos tipo artist segun su nacionalidad
        nacionality = contendrá la nacionalidad de un artista (str)
        resultado = devolvera un conjunto de objetos tipo Artist
        '''
        
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM artista '
        sql += 'WHERE lower(nacionalidad) = lower(?)'
        self.__cursor.execute(sql, (nacionality,))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
            
        return result
    
    
    
    def getBySongType(self, songType):
        '''devuelve una coleccion de objetos tipo artist el genero de algunas de sus canciones
        songType = genero musical (str)
        resultado = devolvera un conjunto de objetos tipo Artist
        '''
        
        sql = 'SELECT distinct artista.id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM artista '
        sql += 'JOIN cancion ON cancion.id_artista = artista.id '
        sql += 'WHERE lower(genero) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{songType}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
            
        return result


    
            
        