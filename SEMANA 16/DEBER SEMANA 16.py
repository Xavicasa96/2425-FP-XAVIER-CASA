# Escritura de archivo de texto
# Abrimos el archivo en modo escritura ('w')
file = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales en el archivo
file.write("Nota 1: Estudiar para el examen.\n")
file.write("Nota 2: Revisar tareas pendientes.\n")
file.write("Nota 3: Comprar comida.\n")

# Cerramos el archivo después de escribir
file.close()

# Lectura del archivo de texto
# Abrimos el archivo en modo lectura ('r')
file = open("my_notes.txt", "r")

# Leemos el contenido del archivo línea por línea
for line in file:
    print(line.strip())  # Imprimimos cada línea y eliminamos saltos de línea

# Cerramos el archivo después de leer
file.close()
