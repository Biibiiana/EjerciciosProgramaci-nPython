# -*- coding: utf-8 -*-
        

class StudentNotFoundError(NameError):
    """Indica que el alumno que se busca no está en la lista.
    Atributos:
    name – nombre del estudiante buscado
    message – texto informativo para el usuario final
    """
    def __init__(self, name, message="El alumno no está en la lista."):
        self.name = name
        self.message = message
     
     
class MarkOutOfRangeError(ValueError):
    """Indica que la nota no está en el rango apropiado.
    Atributos:
    mark – nota del estudiante
    message – texto informativo para el usuario final
    """
    def __init__(self, mark, message="La nota debe estar entre 0 y 10."):
        self.mark = mark
        self.message = message


class Students:
    
    
    def __init__(self, name, mark, phone, email):
        self.name = name
        self.mark = mark
        self.phone = phone
        self.email = email


class List:

    def __init__(self):
        self._students = []


    def add(self, name, mark, phone, email):
        if mark in range(10):
            student = Student(name, mark, phone, email)
            self._students.append(student)
            self._save()
        else:
            raise ValueError            


    def show_students(self,):
        for student in self._students:
            self._print_estudiante(student)


    '''def borrar(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break'''


    def buscar(self, name):
        for student in self._students:
            if student.name.lower() == name.lower():
                self._print_estudiante(student)
                break
        else:
            self._not_found()     
    
    
    def _save(self):
        with open('students.txt', 'w') as f:
            writer = txt.writer(f)
            writer.writerow( ('name', 'mark', 'phone', 'email') )

            for student in self._students:
                writer.writerow( (student.name, student.mark, student.phone, student.email) )


    def _print_estudiante(self, student):
            print('--- * --- * --- * --- * --- *--- *---')
            print('Nombre: {}'.format(student.name))
            print('Nota: {}'.format(student.mark))
            print('telefono: {}'.format(student.phone))
            print('Email: {}'.format(student.email))
            print('--- * --- * --- * --- * --- *--- *---')


    def _not_found(self):
        print('++++++++++++++')
        print('¡Alumno no encontrado!')
        print('+++++++++++++++++')


def run():

    libro_agenda = Agenda()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            libro_agenda.add(row[0], row[1], row[2])


def insert_mark():
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")

'''Meteremos los datos de nombre y nota en una biblioteca y esa biblioteca la metemos
en una lista de diccionarios para tener los nombres y notas relacionados para después
poder extraer los datos cómo necesitemos.'''

def insert_students_data(name, mark, tlf, email, list_students):
    """Insertamos los datos del alumno anteriormente insertados en el sistema 
    en una lista y en """
    studentsdata = {}
    studentsdata["nombre"] = name
    if mark in range(10):
        studentsdata["nota"] = mark
    else:
        
    studentsdata["telefono"] = tlf
    studentsdata["correo_electronico"] = email
    list_students.append(studentsdata)

'''Aqui cogemos cada diccionario que sería i de la lista de estudiante, y cogemos la
nota de i (o sea, el diccionario) y lo añadimos a una nueva lista que esta vez recogerá
todas las notas actuales de los alumnos. Y realizamos la media.'''

def average_of_marks(list_students, list_of_marks):
    for i in list_students:
        list_of_marks.append(i["nota"])
    avg_marks = sum(list_of_marks) / len(list_of_marks)
    return avg_marks

'''Para saber el número de alumnos que han aprobado pasamos por la lista de notas
una por una y vemos si es igual o superior a 5 (lo que contaría cómo aprobados)
y contabilizarlo en la variable passed'''

def pass_students (list_of_marks):
    passed = 0
    for b in list_of_marks:
        if b >= 5:
            passed += 1
    return passed

'''Para saber que laumnos tienen nota sobre la media y saber cuales son cogemos la
lista de estudiantes y la media, cogemos uno a uno los alumnos (sus disccionarios)
y cogiendo su nota de n lo comparamos con la media, si se cumple que su nota es superior
a la media guardamos su nombre y nota en una nueva lista para dársela al usuario.'''

def student_over_average (list_students, average, list_students_over_average):
    for n in list_students:
        if n.get("nota") >= average:
            list_students_over_average.append(n)
    return list_students_over_average

'''Cuando queremos saber la nota sobre un alumno cocreto pasamos por todos los alumnos
de la ista de los mismos y buscamos el alumno del que quieren saber y le damos su nota
al usuario''' 

def data_of_student(list_students, student):
    for n in list_students:
        if n.get("nombre") == student:
            return n.get("nota")

def kjhkh():
    with open("myfile", "rb") as f:
    while (byte := f.read(1)):
        # Do stuff with byte.    
    