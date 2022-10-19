# -*- coding: utf-8 -*-
        

def open_config():
    with open("students.cfg", "r") as f:
        lines = f.readlines()
        names_docs = []
        for i in lines:
            x = i.split("=")
            if "entrada" in x:
                name_entrance = x[1]
            elif "salida" in x:
                name_exit = x[1]
        names_docs = [name_entrance, name_exit]
        return names_docs


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


def show_menu():
    options_menu = [
    	'1. Añadir un estudiante y su calificación. \n'
    	'2. Mostrar una lista de estudiantes con sus calificaciones. \n'
        '3. Calcular la media de toda la clase. \n'
        '4. Calcular el número de aprobados total. \n'
        '5. Mostrar los estudiantes con calificación superior a la media. \n'
        '6. Consultar la nota de un estudiante. \n'
        '7. Terminar de usar el programa. \n'
    ]
    for option in options_menu:
        print(option)


def __init__(self):
    self._students = []


def add(list_students, name, mark, phone, email):
    studentsdata = {}
    if mark in range(10):
        student = Student(name, mark, phone, email)
        list_students.append(student)
    else:
        raise ValueError 
 

def show_students(list_students):
    for student in list_students:
        show_data = _print_estudiante(student)


def average_of_marks(list_students, list_of_marks):
    for i in list_students:
        list_of_marks.append(i["mark"])
    avg_marks = sum(list_of_marks) / len(list_of_marks)
    return avg_marks


def pass_students (list_of_marks):
    passed = 0
    for x in list_of_marks:
        if x >= 5:
            passed += 1
    return passed


def student_over_average (list_students, average, list_students_over_average):
    for n in list_students:
        if n.get("nota") >= average:
            list_students_over_average.append(n)
    return list_students_over_average


'''def borrar(self, name):
    for idx, contact in enumerate(self._contacts):
        if contact.name.lower() == name.lower():
            del self._contacts[idx]
            self._save()
            break'''


def search(list_students, name):
    for student in list_students:
        if student.name.lower() == name.lower():
            show_student = _print_estudiante(student)
            break
    else:
        raise NameError    


def _save(list_students):
    with open('students.txt', 'w') as f:
        writer = txt.writer(f)
        writer.writerow( ('name', 'mark', 'phone', 'email') )

        for student in list_students:
            writer.writerow( (student.name, student.mark, student.phone, student.email) )


def _print_estudiante(list_students, student):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(student.name))
        print('Nota: {}'.format(student.mark))
        print('telefono: {}'.format(student.phone))
        print('Email: {}'.format(student.email))
        print('--- * --- * --- * --- * --- * --- * ---')


'''def _not_found(self):
    print('----------------------')
    print('¡Alumno no encontrado!')
    print('----------------------')'''




