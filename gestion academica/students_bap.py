import pickle
from marks_continuacion_bap import (add, show_students, average_of_marks, pass_students, 
                       student_over_average, search, _save, show_menu, 
                       open_config)

list_students = []
list_students_mark_over_average = []

'''
def ask_for_data_from_students():
    name = input("Introduce el nombre del alumno: ").lower()
    mark = float(input("Ingresa la nota del alumno: "))
    return name, mark
'''

option = None


doc_names = open_config()

print(doc_names)
    


'''
while option != "no":
    if option == "1":
        name, mark, phone, email = ask_for_data_from_students()
        add(list_students, name, mark, phone, email)
    elif option == "2":
        if len(list_students) == 0:
            print("No hay alumnos registrados. ")
        else:
            show_students(list_students)
    elif option == "3":
        list_of_marks = []
        if len(list_students) == 0:
            print("No se puede hacer la media sin notas registradas. ")
        else:
            average = float(average_of_marks(list_students, list_of_marks))
            print("La nota media de todos los alumnos es: ", average)
    elif option == "4": 
        num_pass_students = int(pass_students(list_of_marks))
        print("El número de alumnos que han aprobado es ", num_pass_students)
    elif option == "5":
        if "average" in globals():
            over_average = student_over_average(list_students, average, 
                                                list_students_over_average)
            print("Los alumnos que han superado la media son ", over_average)
        else:
            print("Haz primero la media para concluir lo que desea. ")
    elif option == "6":
        student = input("¿De qué estudiante quieres saber su nota? ").lower()
        if student in list_students:
            mark_of_student = data_of_student(list_students, student)
        else:
            print("Ese alumno no está en el sistema. ")
    elif option == "7":
        option = "no"
    else:
        print("No se encuentra lo que buscas, lo sentimos. ")
    menu = show_menu()
    option = input("¿Qué punto desea hacer?")
    



'''