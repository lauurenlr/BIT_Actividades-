inventario = [{"producto": "camisa", "precio": 25900, "stock": "11"},{"producto": "pantalón", "precio": 39900, "stock": "23"},]

for prod in inventario:
    prod["stock"] = int(prod.get("stock")) #Reading the code, to take the variable "stock" and to convert its numbers to whole numbers
    prod["precio"] = prod["precio"] + 10000 #To review the code, and to add to price 1000
    stock = prod["stock"] #Defining the "stock" variable
    producto = prod["producto"] #Defining the "producto" variable
    precio = prod["precio"]

    print(f"Hay {stock} unidades del producto {producto}. Su precio por unidad es de {precio}") #El print debe estar dentro del ciclo "For" para que se recorra las veces necesarias


