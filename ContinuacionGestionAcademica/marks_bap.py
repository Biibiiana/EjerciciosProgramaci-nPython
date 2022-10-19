import configparser
import os
from pickle import (loads, dumps)


class StudentNotFoundError(IndexError):
    def __init__(self, name, message='--- El alumno no está en la lista.---'):
        self.name = name
        self.message = message
        super().__init__(self.message)


class DataError(IndexError):
    def __init__(self, name, message="El archivo de salida está vacío."):
        self.name = name
        self.message = message
        super().__init__(self.message)


class MarkOutOfRangeError(ValueError):
    def __init__(self, mark, message="La nota debe estar entre 0 y 10."):
        self.mark = mark
        self.message = message
        super().__init__(self.message)


class NotMarkError(IndexError):
    def __init__(self, list_students, message="No hay notas registradas."):
        self.ls = list_students
        self.message = message
        super().__init__(self.message)


class EmptyListError(IndexError):
    def __init__(self, list_marks, message="No hay alumnos registrados."):
        self.lm = list_marks
        self.message = message
        super().__init__(self.message)


def load_config():
    '''Toma el archivo de configuración y devuelve a una lista los nombres de
    los archivos de entrada y salida.'''
    configuracion = configparser.ConfigParser()
    configFilePath = r'students.cfg'
    configuracion.read(configFilePath)
    return [configuracion['FICHEROS']['entrada'],
            configuracion['FICHEROS']['salida']]


def ensure_file_exist(file_path):
    '''Comprueba si los documentos de la configuración están creados
    y si no lo están los crea.'''
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass


def open_txt_file(list_students, list_marks, _entrance):
    '''Toma el nombre del documento de entrada.txt con los estudiantes y
    una lista. Devolviendo el contenido del archivo de texto en la lista.
    Puede dar la excepción FileNotFoundError si el archivo no funciona o
    existe.'''
    _open = open(_entrance)
    lines = _open.readlines()
    for line in lines:
        student_data = line.split(',')
        for number_words in range(len(student_data)):
            student_data[number_words] = student_data[number_words].strip()
        if student_data != ['']:
            name = student_data[0]
            mark = student_data[1]
            email = student_data[2]
            phone = student_data[3]
            add(name.lower(), float(mark), email, int(phone), list_students,
                 list_marks)
    _open.close()


def save_on_binary(list_students, _exit):
    '''Toma el archivo binario de salida y la lista de estudiantes; y traduce
    el contenido de la lista a binario para insertarlo al final del
    archivo.'''
    with open(_exit, 'w') as file:
        content = dumps(list_students)
        file.write(content)


def text_from_binary(_exit):
    '''Toma el archivo binario de salida y traduce su contenido a texto,
    devolviéndolo posteriormente.'''
    with open(_exit, 'rb') as file:
        content = file.read()
        if len(content) != 0:
            return loads(content)
        else:
            raise DataError(_exit)


def update(list_students, list_marks, _entrance):
    """Toma un archivo de texto y una lista y devuelve
    por referencia el contenido del archivo en la lista
    parando el programa si se detecta una excepcion"""
    try:
        open_txt_file(list_students, list_marks, _entrance)
    except FileNotFoundError:
        print("El archivo no funciona o no existe.")
    except MarkOutOfRangeError as MarkOutOfRange:
        print(MarkOutOfRange)
        print("Introduzca nuevos datos")
        raise SystemExit
    except ValueError:
        print("Introduzca un dato numérico en el campo de nota.")
        raise SystemExit


def confirmation(_entrance, _exit, list_students, list_marks):
    '''Se asegura de que el usuario quiere cargar los datos
    desde el archivo de texto y detiene el programa de no ser así'''
    question = input("El archivo " + _exit +
                     " existe\n ¿Añadimos? [S]i o [N]o. ")
    if question == "s" or question == "S":
        update(list_students, list_marks, _entrance)


def show_menu():
    options_menu = [
        '¿Qué opción quiere?\n'
        '[1.] Añadir datos de estudiantes.\n'
        '[2.] Mostrar una lista de estudiantes con sus calificaciones.\n'
        '[3.] Calcular la media de toda la clase.\n'
        '[4.] Calcular el número de aprobados total.\n'
        '[5.] Mostrar los estudiantes con calificación superior a la media.\n'
        '[6.] Consultar la nota de un estudiante.\n'
        '[7.] Terminar de usar el programa.\n'
    ]
    for option in options_menu:
        print(option)


def add(name, mark, phone, email, list_students, list_marks):
    '''Toma la lista de estudiantes y la lista de notas, y tras preguntar por
    los datos que se quieren introducir se añade la información de cada
    estudiante a la lista de estudiantes y las notas a la lista de notas.
    Puede dar la excepción MarkOutOfRangeError si la nota no está entre 0
    y 10.'''
    Student = {}
    if 0 <= mark <= 10:
        Student["nombre"] = name
        Student["nota"] = mark
        Student["telefono"] = phone
        Student["correo"] = email
        list_students.append(Student)
        list_marks.append(mark)
    else:
        raise MarkOutOfRangeError(mark)


def show_students(list_students):
    '''Tomando la lista de estudiantes nos muestra una lista de los mismos
    mediante otra función para dar forma a como mostrar los datos.'''
    if len(list_students) == "0":
        print("No hay alumnos registrados. ")
    else:
        for student in list_students:
            print_student(student)


def marks_average(list_students):
    '''Tomando la lista de estudiantes hacemos la fórmula de la media tomando
    el valor de nota. Puede dar la excepción NotMarkError en el caso de que
    no haya notas registradas.'''
    marks = 0
    if list_students:
        for student in list_students:
            marks += student["nota"]
        average_mark = float(marks) / len(list_students)
        return average_mark
    else:
        raise NotMarkError(list_students)


def pass_students(list_marks):
    '''Tomando la lista de notas comprobamos cuantos están aprobados. Puede
    dar la excepción EmptyListError en el caso de que la lista de notas este
    vacía.'''
    passed = 0
    if list_marks:
        for mark in list_marks:
            if mark >= 5:
                passed += 1
        return passed
    else:
        raise EmptyListError(list_marks)


def above_average_student(list_students, average):
    '''Tomando la lista de estudiantes y la media comprobamos quienes están
    sobre la media. Puede dar la excepción NotMarkError en el caso de que
    no haya notas registradas.'''
    above_average_students = []
    if list_students:
        for student in list_students:
            if student.get("nota") >= average:
                above_average_students.append(student)
        return above_average_students
    else:
        raise NotMarkError(list_students)


def search(list_students, student):
    '''Tomando la lista de estudiantes y el estudiante que nos facilita el
    usuario comprobamos si está en nuestra lista y si es así devolvemos su
    nota. Puede dar la excepción StudentNotFoundError en el caso de que
    no se encuentre el estudiante.'''
    for student_data in list_students:
        if student_data.get("nombre") == student:
            return student_data.get("nota")
    raise StudentNotFoundError(student)


def print_student(student):
    print("--- * --- * --- * --- * --- * --- * ---")
    print("Nombre: {}".format(student["nombre"]))
    print("Nota: {}".format(student["nota"]))
    print("telefono: {}".format(student["telefono"]))
    print("Email: {}".format(student["correo"]))
    print("--- * --- * --- * --- * --- * --- * ---")
