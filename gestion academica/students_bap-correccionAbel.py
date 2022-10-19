# -*- coding: utf-8 -*-

import marks_bap
from marks_bap import (insert_name_mark, average_of_marks, pass_students, student_over_average, data_of_student)


def pedir_datos_alumno():
    name = input("Introduce el nombre del alumno: ").lower()
    mark = float(input("Ingresa la nota del alumno: "))
    return name, mark


opciones_menu = (
	'1. Añadir un estudiante y su calificación.'
	'2. Mostrar una lista de estudiantes con sus calificaciones.'
)

def presentar_menu()
	for opcion in opciones_menu:
		print(opcion)

list_students = []
list_students_over_average = []

data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()

while data != "no":
    if data == "1":
	'''
        name = input("Introduce el nombre del alumno: ").lower()
        mark = float(input("Ingresa la nota del alumno: "))
        insert_name_mark(name, mark, list_students)
	'''
        name, mark = pedir_datos_alumno()
	insert_name_mark(name, mark, list_students)
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "2":
        if len(list_students) == 0:
            print("No hay alumnos registrados. ")
        else:
            print("Aquí están todos los alumnos: \n", list_students)
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "3":
        list_of_marks = []
        if len(list_students) == 0:
            print("No se puede hacer la media sin notas registradas. ")
        else:
            average = float(average_of_marks(list_students, list_of_marks))
            print("La nota media de todos los alumnos es: ", average)
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "4": 
        num_pass_students = int(pass_students(list_of_marks))
        print("El número de alumnos que han aprobado es de ", num_pass_students)
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "5":
        if "average" in globals():
            over_average = student_over_average(list_students, average, list_students_over_average)
            print("Los alumnos que han superado la media es de ", over_average)
        else:
            print("Haz primero la media para concluir lo que desea. ")
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "6":
        student = input("¿De qué estudiante quieres saber su nota? ").lower()
        if student in list_students:
            mark_of_student = data_of_student(list_students, student)
            print("La nota del estudiante ", student, " es: ", mark_of_student)
        else:
            print("Ese alumno no está en el sistema. ")
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()
    elif data == "7":
        data = "no"
    else:
        print("No se encuentra lo que buscas, lo sentimos. ")
        data = input("1. Añadir un estudiante y su calificación. \n2. Mostrar una lista de estudiantes con sus calificaciones. \n3. Calcular la media de toda la clase. \n4. Calcular el número de aprobados total. \n5. Mostrar los estudiantes con calificación superior a la media. \n6. Consultar la nota de un estudiante. \n7. Terminar de usar el programa. \n- ").lower()



