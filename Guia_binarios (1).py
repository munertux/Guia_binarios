print('Tienes que elegir la base del numero que quieres ingresar')
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Base 2', accion1),
        '2': ('Base 8', accion2),
        '3': ('Base 10', accion3),
        '4': ('Base 16', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    print('------------------------------------------')
    print('Has elegido ingresar un numero con base 2')
    def binario_a_decimal(binario):
        posicion = 0
        decimal = 0
        binario = binario[:-1]
        for digito in binario:
            multiplicador = 2**posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal
    binario = input("Ingresa un numero binario: ")
    decimal = binario_a_decimal(binario)
    def decodificar(mensaje):
        numeros = mensaje.split(",")
        decodificado = ""
        for numero_binario in numeros:
            numero_decimal = int(numero_binario, 2)
            letra = chr(numero_decimal)
            decodificado += letra
        return decodificado
    codificado = binario
    decodificado = decodificar(codificado)
    print('------------------------------------------')
    print("Binario es: ")
    print(binario)
    print("Decimal es: ")
    print(decimal)
    print("Decodificado es: ")
    print(decodificado)
    print('------------------------------------------')
def accion2():
    print('------------------------------------------')
    print('Has elegido ingresar un numero con base 8')
    def octal_a_decimal(octal_1):
        decimal_1 = 0
        posicion_1 = 0
        octal_1 = octal_1[:-1]
        for digito in octal_1:       
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion_1)
            equivalencia = int(numero_elevado * valor_entero)
            decimal_1 += equivalencia
            posicion_1 += 1
        return decimal_1
    octal_1 = input("Ingresa un número octal: ")
    decimal_1 = octal_a_decimal(octal_1)

    def decimal_a_binario(decimal_1):
        if decimal_1 <= 0:
            return "0"
        binario_1 = ""
        while decimal_1 > 0:
            residuo = int(decimal_1 % 2)
            decimal_1 = int(decimal_1 / 2)
            binario_1 = str(residuo) + binario_1
        return binario_1
    
    
    binario_1 = decimal_a_binario(decimal_1)

    def decodificar_1(mensaje):
        numeros = mensaje.split(",")
        decodificado_1 = ""
        for numero_binario in numeros:
            numero_decimal = int(numero_binario, 2)
            letra = chr(numero_decimal)
            decodificado_1 += letra
        return decodificado_1
    codificado_1 = binario_1
    decodificado_1 = decodificar_1(codificado_1)    
    print('------------------------------------------')
    print("Octal es: ")
    print(octal_1)
    print("Decimal es: ")
    print(decimal_1)
    print("Decodificado es: ")
    print(decodificado_1)
    print('------------------------------------------')
def accion3():
    print('------------------------------------------')
    print('Has elegido ingresar un numero con base 10')
    def decimal_a_binario_1(decimal_2):
        if decimal_2 <= 0:
            return "0"
        binario_2 = ""
        while decimal_2 > 0:
            residuo_1 = int(decimal_2 % 2)
            decimal_2 = int(decimal_2 / 2)
            binario_2 = str(residuo_1) + binario_2
        return binario_2


    decimal_2 = int(input("Ingresa un número decimal: "))
    binario_2 = decimal_a_binario_1(decimal_2)


    def decodificar_2(mensaje_1):
        numeros_1 = mensaje_1.split(",")
        decodificado_2 = ""
        for numero_binario_1 in numeros_1:
            numero_decimal_1 = int(numero_binario_1, 2)
            letra_1 = chr(numero_decimal_1)
            decodificado_2 += letra_1
        return decodificado_2
    codificado_2 = binario_2
    decodificado_2 = decodificar_2(codificado_2)
    print('------------------------------------------')
    print("Decimal es: ")
    print(decimal_2)
    print("Decodificado es: ")
    print(decodificado_2)       
    print('------------------------------------------')
def accion4():
    print('------------------------------------------')
    print('Has elegido ingresar un numero con base 16')
    def obtener_valor_real(caracter_hexadecimal):
        equivalencias = {
            "f": 15,
            "e": 14,
            "d": 13,
            "c": 12,
            "b": 11,
            "a": 10,
        }
        if caracter_hexadecimal in equivalencias:
            return equivalencias[caracter_hexadecimal]
        else:
            return int(caracter_hexadecimal)


    def hexadecimal_a_decimal(hexadecimal):
        hexadecimal = hexadecimal.lower()
        hexadecimal = hexadecimal[:-1]
        decimal_3 = 0
        posicion_1 = 0
        for digito in hexadecimal:
            valor = obtener_valor_real(digito)
            elevado_1 = 16 ** posicion_1
            equivalencia_1 = elevado_1 * valor
            decimal_3 += equivalencia_1
            posicion_1 += 1
        return decimal_3
    hexadecimal = input("Ingresa un número hexadecimal: ")
    decimal_3 = hexadecimal_a_decimal(hexadecimal)


    def decimal_a_binario_2(decimal_3):
        if decimal_3 <= 0:
            return "0"
        binario_3 = ""
        while decimal_3 > 0:
            residuo_2 = int(decimal_3 % 2)
            decimal_3 = int(decimal_3 / 2)
            binario_3 = str(residuo_2) + binario_3
        return binario_3


    binario_3 = decimal_a_binario_2(decimal_3)


    def decodificar_3(mensaje_2):
        numeros_2 = mensaje_2.split(",")
        decodificado_3 = ""
        for numero_binario_2 in numeros_2:
            numero_decimal_2 = int(numero_binario_2, 2)
            letra_2 = chr(numero_decimal_2)
            decodificado_3 += letra_2    
        return decodificado_3
    codificado_3 = binario_3
    decodificado_3 = decodificar_3(codificado_3)
    print('------------------------------------------')
    print("Hexadecimal es: ")
    print(hexadecimal)
    print("Decimal es: ")
    print(decimal_3)
    print("Decodificado es: ")
    print(decodificado_3)    
    print('------------------------------------------')
def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()