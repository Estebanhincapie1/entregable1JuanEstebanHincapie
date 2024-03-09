def obtener_nombre():
    while True:
        nombre = input("Por favor, ingresa el nombre: ")
        if nombre.replace(" ", "").isalpha() == True:
            return nombre
        else:
            print('Ingrese un dato valido, sin caracteres raros')
            continue

from datetime import datetime

def validar_fecha(fecha_str):
    try:
        # Intenta convertir la cadena en un objeto de fecha
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        return True, fecha
    except ValueError:
        # Si hay un error en la conversión, la fecha no es válida
        return False, None


def pedir_fecha(mns):
    fecha_valida = False
    while not fecha_valida:
        fecha_str = input(mns +"Por favor, introduce una fecha en formato dd/mm/aaaa: ")
        fecha_valida, fecha = validar_fecha(fecha_str)
        if not fecha_valida:
            print("Fecha inválida. Por favor, inténtalo de nuevo.")
    return fecha


def datoEntero(mns):
    while True:
        dato = input(mns)
        if dato.isnumeric() == True:
            return int(dato)
        else:
            print('DATO ERRONEO, POR FAVOR INTENTE DE NUEVO')
            continue

def datoFloat(mns):
    while True:
        try:
            dato = float(input(mns))
            return dato
        except ValueError:
            print('dato erroneo')
            continue
        
