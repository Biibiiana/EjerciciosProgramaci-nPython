import sys
from pickle import UnpicklingError
from marks_bap_continuacion import(load_config, text_from_binary,
                                   confirmation, show_menu, DataError,
                                   show_students, marks_average,
                                   pass_students, above_average_student,
                                   search, save_on_binary)

list_students = []
option = None
list_marks = []
average = -1
_entrance = ""
_exit = ""

try:
    _open = load_config()
    print(_open)
    _entrance = _open[0]
    _exit = _open[1]
except FileExistsError:
    print("El archivo de configuración no existe.")
except FileNotFoundError:
    print("El archivo de configuración no funciona.")
else:
    try:
        list_students = text_from_binary(_exit)
    except DataError as d:
        print(d)
    except FileNotFoundError:
        print (str("_exit") + " no encontrado.")
    except UnpicklingError:
        print("Datos corruptos o no legibles.")
    # Datos cargados.
    if sys.argv[1] == "1":
        confirmation(_entrance, _exit, list_students, list_marks)
    elif sys.argv[1] == "2":
            show_students(list_students)
    elif sys.argv[1] == "3":
        try:
            average = marks_average(list_students)
            print("La nota media de todos los alumnos es " + str(average))
        except ZeroDivisionError:
            print("No se puede hacer la media sin notas registradas.")
    elif sys.argv[1] == "4":
        try:
            num_pass_students = pass_students(list_marks)
            print("El número de aprobados es " + str(num_pass_students))
        except ZeroDivisionError:
            print("No se puede hacer la media sin notas registradas.")
    elif sys.argv[1] == "5":
        try:
            above_average = above_average_student(list_students, average)
            print("Alumnos que superan la media" + str(above_average))
        except ZeroDivisionError:
            print("Haz primero la media para concluir lo que desea.")
    elif sys.argv[1] == "6":
        student = input("¿De quién quieres saber la nota? ").lower()
        mark_of_student = search(list_students, student)
        print("La nota de " + str(student) + " es " + str(mark_of_student))
    elif sys.argv[1] == "7":
        save_on_binary(list_students, _exit)
        option = "0"
        print("Hasta la próxima.")
    else:
        print("Lo sento no le he entendido, elija uno de los siguientes.")
        menu = show_menu()
        option = input("¿Qué opción quiere? ")
