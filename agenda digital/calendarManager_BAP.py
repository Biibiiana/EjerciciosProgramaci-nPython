import sqlite3


class CalendarManager:
    '''Gestiona los objetos de la clase Contact en la base de datos'''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()
    
    
    def getByDate(self, date):
        '''devuelve una coleccion de objetos tipo cita segun su fecha
        Parámetros:
            date = contendrá una fecha de una cita (str)
        Devuelve:
            Un conjunto de objetos tipo Calendar
        '''
        
        sql = 'SELECT ci.cita_id, ci.descripcion, ci.lugar, ci.fecha, co.name '
        sql += 'FROM cita ci, contacto co, contactos_cita cc '
        sql += 'WHERE ci.fecha = ? AND cc.id_cita = ci.cita_id '
        sql += 'AND cc.id_contacto = co.contacto_id'
        self.__cursor.execute(sql, (f'%{date}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
            
    
    
    def getByAddress(self, address):
        '''devuelve una coleccion de objetos tipo cita segun su direccion
        Parámetros:
            address = contendrá una direccion de una cita (str)
        Devuelve:
            Un conjunto de objetos tipo Calendar
        '''
        
        sql = 'SELECT ci.cita_id, ci.descripcion, ci.lugar, ci.fecha, co.name '
        sql += 'FROM cita ci, contacto co, contactos_cita cc '
        sql += 'WHERE ci.lugar = ? AND cc.id_cita = ci.cita_id '
        sql += 'AND cc.id_contacto = co.contacto_id'
        self.__cursor.execute(sql, (f'%{address}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
    
    
    def getByContacts(self, contact):
        '''devuelve una coleccion de objetos tipo cita segun su fecha
        Parámetros:
            contact = contendrá un nombre de un contacto (str)
        Devuelve:
            Un conjunto de objetos tipo Calendar
        '''
        
        sql = 'SELECT ci.cita_id, ci.descripcion, ci.lugar, ci.fecha, co.name '
        sql += 'FROM cita ci, contacto co, contactos_cita cc '
        sql += 'WHERE co.name = ? AND cc.id_cita = ci.cita_id '
        sql += 'AND cc.id_contacto = co.contacto_id'
        self.__cursor.execute(sql, (f'%{contact}%',))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result


myConnection = sqlite3.connect('AgendaDigital_BAP.db')

manager = CalendarManager(myConnection)
print('Los contactos de su consulta son: \n', manager.getBydate('06/02/2023'))
print('Los contactos de su consulta son: \n', manager.getByAddress('S/N'))
print('Los contactos de su consulta son: \n', manager.getBycontact('Bibi'))
        