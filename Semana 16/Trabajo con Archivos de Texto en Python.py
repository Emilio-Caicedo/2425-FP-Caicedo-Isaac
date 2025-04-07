# Escritura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo escritura ('w').
# Si el archivo no existe, se crea automáticamente.

with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Me encuentro finalizando con éxito el primer semestre y me siento orgulloso del progreso que he logrado.\n")
    file.write("Aprendí mucho sobre programación y adquirí habilidades valiosas que me motivan a seguir adelante.\n")
    file.write("Despúes de los exámenes me tomaré un merecido descanso para poder comenzar el segundo semestre con más energía.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')

file = open('my_notes.txt', 'r')

# Usamos un bucle para leer y mostrar cada línea del archivo

print("Contenido del archivo:")
linea = file.readline()
while linea:
    print(linea.strip())  # .strip() elimina los saltos de línea extra al imprimir
    linea = file.readline()

# Cierre del archivo

file.close()
