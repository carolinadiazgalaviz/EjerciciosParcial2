name = []
idUsuario = []
email = []
age = []
identification = []
genre = []
range = []
password = []
confirmPass = []
option = 0

while True:
 print("Bienvenido al sistema de registro de usuarios.")
print("1. Registrar usuario")
print("2. Salir")
print("3. Borrar información de usuario")
print("4. Mostrar información de usuario")
print("5. Salir del programa")
option = int(input("Seleccione una opción: "))
match option:
    case 1:
        name.append(input("Ingrese el nombre del usuario: "))   
        idUsuario = int(input("Ingrese el ID del usuario: "))
        email = input("Ingrese el correo electrónico del usuario: ")
        age = int(input("Ingrese la edad del usuario: "))
        identification = input("Ingrese la identificación del usuario: ")
        genre = input("Ingrese el género del usuario: ")
        range = int(input("Ingrese el rango del usuario (0 para usuario normal, 1 para administrador): "))
        password = input("Ingrese la contraseña del usuario: ")
        confirmPass = input("Confirme la contraseña del usuario: ")
        if password != confirmPass:
            print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
    case 2:
        print("Nombre:", name, "Edad:", age, "Correo electrónico:", email)
    case 3:
        name = ""
        idUsuario = 0
        email = ""
        age = 0
        identification = ""
        genre = ""
        range = 0
        password = ""
        confirmPass = ""
    case 4:
        name = input("Ingrese el nombre del usuario: ")
        idUsuario = int(input("Ingrese el ID del usuario: "))
        email = input("Ingrese el correo electrónico del usuario: ")
        age = int(input("Ingrese la edad del usuario: "))
        identification = input("Ingrese la identificación del usuario: ")
        genre = input("Ingrese el género del usuario: ")
        range = int(input("Ingrese el rango del usuario (0 para usuario normal, 1 para administrador): "))
        password = input("Ingrese la contraseña del usuario: ")
        confirmPass = input("Confirme la contraseña del usuario: ")
    case 5:
        print("¡Hasta luego!")
        break
    case _:
        print("Opción no válida")