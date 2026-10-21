nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18:# el if va seguido de la condición y luego de los dos puntos
    print("Eres mayor de edad.")
else:#el else va seguido de dos puntos para decir que se hace si no se cumple la condición del if
    print("No eres mayor de edad.")

if nacionalidad == "N":
        print("Esta persona es de nacionalidad mexicana")
else:
    print("Esta persona no es de nacionalidad mexicana")