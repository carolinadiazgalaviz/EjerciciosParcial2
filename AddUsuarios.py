name = "Manuel"
idUsuario = 123456
email = "manuel@example.com"
age = 30
identification = "123456789"
genre = "Masculino"
range = 0
password = "password123"
confirmPass = "password123"

name = input("Ingrese el nombre del usuario: ")
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

