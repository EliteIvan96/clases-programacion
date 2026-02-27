#El Reto: "Mi Carrito de Supermercado"
#Escribe un programa en Python que haga lo siguiente:
#Crea una lista llamada carrito que tenga inicialmente 3 productos (por ejemplo: "pan", "leche", "huevos").
#Agrega un nuevo producto al final de la lista usando .append().
# Modifica el segundo elemento de la lista (el que está en el índice 1) por otro producto distinto.
#Elimina el primer elemento de la lista.
#Imprime cuántos productos hay en total usando len() (len funciona para obtener el N elementos de tu lista).
#Usa un bucle for para mostrar cada producto con un mensaje que diga: f"Tengo que comprar: {producto}".

carrito =[ "pan", "leche", "huevos"]
#agrega un producto a la lista .append()
carrito.append("Queso")
print(carrito)
#modifica un elemento de la lista 
carrito[1] = "Jamon"
print(carrito)
#Eliminar el primer elemento de la lista 
carrito.remove("pan")
print(carrito)
#Imprime cuántos productos hay en total usando len() (len funciona para obtener el N elementos de tu lista).
longitud=len(carrito)
print(longitud)


for i in range(len(carrito)):
    print (f"Tengo que comprar : {carrito[i]}")

