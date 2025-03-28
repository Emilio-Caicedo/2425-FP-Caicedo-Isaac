# Trabajando con Diccionarios en Python.

# Crear un diccionario con información personal

informacion_personal = {
    "Nombre": "Moisés Caicedo",
    "Edad": 23,
    "Ciudad": "Santo Domingo",
    "Profesion": "Futbolista"
}

# Acceder y modificar el valor de la clave "Ciudad"

informacion_personal["Ciudad"] = "Nueva Loja"

# Agregar una nueva clave-valor para la Profesion (ya existe, pero se mantiene el requerimiento)

informacion_personal["Profesion"] = "Desarrollador de Software"

# Verificar si la clave "Convencional" existe en el diccionario, si no, agregarla

if "telefono" not in informacion_personal:
    informacion_personal["Convencional"] = "063020173"

# Eliminar la clave "Edad" del diccionario

del informacion_personal["Edad"]

# Imprimir el diccionario final

print(informacion_personal)
