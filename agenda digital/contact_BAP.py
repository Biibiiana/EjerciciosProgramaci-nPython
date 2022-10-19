import sqlite3


class Contact:
    '''
    Representa a un contacto.
    '''

    def __init__(self, connection, file=None, contacto_id=None, nombre=None,
    apellidos=None, correo=None, telefono=None, direccion=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__file = file
        self.__id = contacto_id
        self.__name = nombre
        self.__surname = apellidos
        self.__email = correo
        self.__phone = telefono
        self.__address = direccion


    def __str__(self):
        return f'El contacto con nombre {self.__name} y apellidos {self.__surname}'


    def getId(self):
        return self.__id


    def save(self):
        '''
        Añade un nuevo artista a la base de datos.
        '''
        sql = 'INSERT INTO contacto (nombre, apellidos, correo, telefono, '
        sql += 'direccion) VALUES (?, ?, ?, ?, ?)'
        values = (
            self.__name,
            self.__surname,
            self.__email,
            self.__phone,
            self.__address,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
        return('El contacto se ha añadido.\n')


    def add_contact(self):
        '''
        Función que añade un contacto de un fichero dado.
        Parámetros:
            file: Es un fichero con los datos del contacto.
        Devuelve:
            Un mesaje informando sobre si el contacto se ha añadido 
            o ha habido algún problema.
        '''
        try: 
            f = open(self.__file, 'r')
        except FileNotFoundError:
            return('¡El fichero ' + self.__file + ' no existe!\n')
        else:
            lines = f.readlines()
            for line in lines:
                if not line.isspace():
                    contacts_data = line.split(',')
                    if contacts_data != ['']:
                        name = contacts_data[0].strip()
                        surname = contacts_data[1].strip()
                        email = contacts_data[2].strip()
                        phone = contacts_data[3].strip()
                        address = contacts_data[4].strip()
                        sql = 'INSERT INTO Contacto (nombre, apellidos, '
                        sql += 'correo, telefono, direccion) '
                        sql += 'VALUES (?, ?, ?, ?, ?)'
                        values = (
                            name or None,
                            surname or None,
                            email or None,
                            phone or None,
                            address or None,
                        )
                        self.__cursor.execute(sql, values)
                        self.__connection.commit()
            f.close()
            return('El contacto se ha añadido.\n')


    def update(self, id):
        '''
        Actualiza los datos de un contacto existente en la base de datos.
        '''
        if id is None:
            raise TypeError('El atributo id debe tener valor')
        else:
            sql = 'UPDATE contacto SET nombre = ?, apellidos = ?, '
            sql += 'correo = ?, telefono = ?, direccion = ? '
            sql += 'WHERE telefono = ?'
            values = (
                self.__name,
                self.__surname,
                self.__email,
                self.__phone,
                self.__address,
                id,
            )
            self.__cursor.execute(sql, values)
            self.__connection.commit()
        return('El contacto se ha actualizado.\n')


    def delete(self):
        '''
        Borra un contacto existente en la base de datos.
        '''
        sql = 'DELETE FROM contacto WHERE id_contacto = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
        return('El contacto se ha eliminado.\n')


myConnection = sqlite3.connect('AgendaDigital_BAP.db')

contacto = Contact(myConnection, None, None, 'Bibiana', 'Antequera', 'bibi@correo.es', '666555444', None)
print(contacto.save())


file = "contacts.txt"
contacto = Contact(myConnection, file)
print(contacto.add_contact())

contacto = Contact(myConnection, None, None, 'Bibiana', 'Antequera Palacios', 'bibi@correo.es', '666555444', None)
print(contacto.update('1'))


contacto = Contact(myConnection, None, '110', None, None, None, None, None)
print(contacto.delete())
