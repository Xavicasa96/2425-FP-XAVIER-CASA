# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "CUENCA",
    "profesion": "Ingeniero"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "GUAYAQUIL"

# Agregar el teléfono si no existe
informacion_personal["telefono"] = "0962311159"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
