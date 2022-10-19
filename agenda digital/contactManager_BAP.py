import sqlite3


class ContactManager:
    '''Gestiona los objetos de la clase Contact en la base de datos'''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()
    
    
    def getByName(self, name):
        '''devuelve una coleccion de objetos tipo contacto segun su nombre
        Parámetros:
            name = contendrá un nombre o parte de él de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Contact
        '''
        
        sql = 'SELECT id_contacto, nombre, apellidos, correo, telefono, '
        sql += 'direccion FROM contacto '
        sql += 'WHERE lower(nombre) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{name}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
            
    
    
    def getBySurname(self, surname):
        '''devuelve una coleccion de objetos tipo contacto segun su apellido/s
        Parámetros:
            surname = contendrá un apellido o parte de él de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Contact
        '''
        
        sql = 'SELECT id_contacto, nombre, apellidos, correo, telefono, '
        sql += 'direccion FROM contacto '
        sql += 'WHERE lower(apellidos) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{surname}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
    
    
    def getByEmail(self, email):
        '''devuelve una coleccion de objetos tipo contacto segun su correo
        Parámetros:
            email = contendrá parte del correo de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Contact
        '''
        
        sql = 'SELECT id_contacto, nombre, apellidos, correo, telefono, '
        sql += 'direccion FROM contacto '
        sql += 'WHERE lower(correo) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{email}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
    
    
    def getByPhone(self, phone):
        '''devuelve una coleccion de objetos tipo contacto segun su telefono
        Parámetros:
            phone = contendrá parte del telefono de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Contact
        '''
        
        sql = 'SELECT id_contacto, nombre, apellidos, correo, telefono, '
        sql += 'direccion FROM contacto '
        sql += 'WHERE lower(telefono) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{phone}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
    
    
    def getByAddress(self, address):
        '''devuelve una coleccion de objetos tipo contacto segun su direccion
        Parámetros:
            address = contendrá parte de la direccion de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Contact
        '''
        
        sql = 'SELECT id_contacto, nombre, apellidos, correo, telefono, '
        sql += 'direccion FROM contacto '
        sql += 'WHERE lower(direccion) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{address}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result


myConnection = sqlite3.connect('AgendaDigital_BAP.db')

manager = ContactManager(myConnection)
print('Los contactos de su consulta son: \n', manager.getByName('Bibiana'))
print('Los contactos de su consulta son: \n', manager.getBySurname('Ant'))
print('Los contactos de su consulta son: \n', manager.getByEmail('correo'))
print('Los contactos de su consulta son: \n', manager.getByPhone('66'))
print('Los contactos de su consulta son: \n', manager.getByAddress('S/N'))
        