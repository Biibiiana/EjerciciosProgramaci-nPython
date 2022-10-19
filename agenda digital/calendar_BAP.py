class Calendar:
    '''
    Representa una cita dentro de un calendario.
    '''

    def __init__(self, connection, cita_id=None, descripcion=None, lugar=None, 
                 fecha=None, *contactos):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = cita_id
        self.__description = descripcion
        self.__address = lugar
        self.__date = fecha
        self.__contacts = contactos

    
    def __str__(self):
        return f'La cita {self.__description} será en {self.__address} el día {self.__date} a las {self.__hour}'
    
    
    def getId(self):
        return self.__id


    def save(self):
        '''
        Añade una cita en la base de datos.
        '''
        sql = 'INSERT INTO Cita (id_cita, descripcion, lugar, fecha, '
        sql += 'contactos) VALUES (?, ?, ?, ?, ?)'
        values = (
            self.__id,
            self.__description,
            self.__address,
            self.__date,
            self.__contacts,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra una cita existente en la base de datos.
        '''
        sql = 'DELETE FROM Cita WHERE id_cita '
        self.__cursor.execute(sql, (self.__date,self.__hour,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de una cita en la base de datos.
        '''
        if self.__description is None:
            raise TypeError('El atributo descripcion debe tener valor')
        sql = 'UPDATE Cita SET descripcion = ?, lugar = ?, fecha = ?,'
        sql += 'contactos = ? WHERE fecha = ?'
        values = (
            self.__id,
            self.__description,
            self.__address,
            self.__date,
            self.__contacts,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()