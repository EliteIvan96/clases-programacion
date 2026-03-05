estudiantes = {
    'A001': { "nombre": "EDGAR", "edad": 23, "promedio": 8.5 },
    'A002': { "nombre": "KAREN", "edad": 29, "promedio": 7.5 },
    'A003': { "nombre": "ESMERALDA", "edad": 20, "promedio": 4.5 }
}

#PARTE 1 — INSERTAR DATOS
#1.- Agrega manualmente al menos 3 estudiantes al diccionario.
#2.- Imprime el diccionario completo.
# INSERTAR UN NUEVO ELEMENTO EN EL DICCIONARIO

#paises_capitales['Chile'] = 'Santiago de Chile'

estudiantes["A004"] = { "nombre": "JUAN","edad": 14,"promedio": 6.5 }
estudiantes["A005"] = { "nombre": "MIGUEL","edad": 30,"promedio": 4.5 }
estudiantes["A006"] = { "nombre": "FELIPE","edad": 35,"promedio": 8.5 }
#print(estudiantes)

#for mat, val in estudiantes.items():
 #print(f"MATRICULA: {mat}: {val['nombre']}, EDAD: {val['edad']}, PROMEDIO: {val['promedio']}")

print(f"Encuentra el alumno con mayor promedio ")
promedio = max(estudiantes[mat]["promedio"] for mat in estudiantes)
print("El mayor promedio es:", promedio)
   




