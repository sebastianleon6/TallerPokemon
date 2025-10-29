#variables

usuario = "Usuario1"
passt = "123456"
intentos = 0
ini = False

## Inicio de sesión "  Parte 1. Inicio de sesión  "  ##

print("")
print(" Hola, en que te puedo ayudar el dia de hoy ")
input()
print("")
print("Antes de ayudarte ingresa tu usaurio y contraseña")
print("")

while intentos < 3:
    
    usu = input("Ingresa usuario: ")
    contra = input("Ingresa tu contraseña ")
    print("")
    
    if usu == usuario and contra == passt:

        ini = print("Inicio de Sesón Correcto")
        ini = True

        break

    else:
         
         print("Usuario o contraseña incorrecta, digitalo nuevamnete")
         print("")

    intentos += 1

if ini == True:

    print("")
    print("Bien venido")
    print("")

else:

    print("*** Usaurio bloqueado ****")
    print("")


## Inicio de sesión 2 "  Parte 2. Menú principal  "##

datos_personales = {"nombre": "Sebastian", "edad": 25, "color_favorito": "azul"}

menu2 = True

while menu2:

    print("")
    print("MENÚ PRINCIPAL")
    print("")
    print("1. Información")
    print("2. Agregar datos")
    print("3. Eliminar datos")
    print("4. Realizar cálculos")
    print("5. Cerrar sesión")
  

    opcionMenu = input("Elige una opción: ")

    if opcionMenu == "1":
        print("Has elegido 'Información'")
        print("")
        print("la informacion que tienes es: ")
        for clave, valor in datos_personales.items():
            print(f"{clave}: {valor}")

    elif opcionMenu == "2":
        print("Has elegido 'Agregar datos'")
        print("Agregar nuevos datos")
        clave = input("Ingresa el nombre del dato que deseas agregar: ")
        valor = input("Ingresa el valor: ")
        datos_personales[clave] = valor
        print(f"Dato agregado: {clave} = {valor}")

    elif opcionMenu == "3":
        print("Has elegido 'Eliminar datos'")
        print("Eliminar datos")
        clave = input("Ingresa el nombre del dato que deseas eliminar: ")
        if clave in datos_personales:
            del datos_personales[clave]
            print(f"Dato '{clave}' eliminado correctamente.")
        else:
            print(f"No existe ningún dato con el nombre '{clave}'.")

    elif opcionMenu == "4":
        print("")
        print("Has elegido 'Realizar cálculos'")
        print("")
        print("¿ Que calculo deseas realizar ? Escribe Suma, Resta, Multiplicación o División")
        print("")
        operacion = input(": ")

        if operacion == "Suma":
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")

        elif operacion == "Resta:":

            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            resultado = num1 - num2
            print(f"El resultado de la Resta es: {resultado}")

        elif operacion == "Multiplicación":
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            resultado = num1 * num2
            print(f"El resultado de la Multiplicación es: {resultado}")

        elif operacion == "División":
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            resultado = num1 / num2
            print(f"El resultado de la División es: {resultado}")
        else: 
            print("Datos incorrectos")
            
    elif opcionMenu == "5":
        print("Cerrando sesión...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

        

    