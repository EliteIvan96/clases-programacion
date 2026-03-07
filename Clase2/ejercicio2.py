estudiantes = {
    'A001': { "nombre": "EDGAR", "edad": 23, "promedio": 8.5 },
    'A002': { "nombre": "KAREN", "edad": 29, "promedio": 7.5 },
    'A003': { "nombre": "ESMERALDA", "edad": 20, "promedio": 4.5 }
}


"""PARTE 5 — ELIMINAR ESTUDIANTE

1.- Solicita una matrícula.
2.- Si existe, elimínala del diccionario usando del.
3.- Muestra el diccionario final.
"""

mat = input("ingresa la matricula :")
del estudiantes[mat]
print(estudiantes) 






