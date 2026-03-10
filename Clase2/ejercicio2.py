
"""PARTE 6 — ANÁLISIS

1.- Encuentra el estudiante con mayor promedio.
2.- Calcula el promedio general del grupo.
3.- Muestra los resultados en pantalla."""

estudiantes = {
    'A001': { "nombre": "EDGAR", "edad": 23, "promedio":2.2 },
    'A002': { "nombre": "KAREN", "edad": 29, "promedio": 7.5 },
    'A003': { "nombre": "ESMERALDA", "edad": 20, "promedio": 4.5 }
}
# Variables para el mayor promedio
mayor_promedio = 0
# Recorrer el diccionario
for matricula in estudiantes:
    promedio = estudiantes[matricula]["promedio"]

    if promedio > mayor_promedio:
        mayor_promedio = promedio
       # print(promedio)

suma = estudiantes['A001']['promedio'] + estudiantes['A002']['promedio'] + estudiantes['A003']['promedio']
print("El Mayor promedio de la clase es :", mayor_promedio)
print("El promedio general del grupo es :", suma / len(estudiantes))





