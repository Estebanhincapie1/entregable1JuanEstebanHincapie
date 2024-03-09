def obtener_nombre():
    nombre = input("Por favor, ingresa tu nombre: ")
    
    # Validar que el nombre no contenga caracteres especiales ni números
    if not nombre.replace(" ", "").isalpha():
        print("El nombre no puede contener caracteres especiales, números ni espacios adicionales.")
        return obtener_nombre()  # Llamada recursiva para solicitar un nuevo nombre
    else:
        # Convertir el nombre a minúsculas
        nombre = nombre.lower()
        return nombre


from datetime import datetime

def validar_fecha(fecha_str):
    try:
        # Intenta convertir la cadena en un objeto de fecha
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        return True, fecha
    except ValueError:
        # Si hay un error en la conversión, la fecha no es válida
        return False, None


def pedir_fecha():
    fecha_valida = False
    while not fecha_valida:
        fecha_str = input("Por favor, introduce una fecha en formato dd/mm/aaaa: ")
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
        
