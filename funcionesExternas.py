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