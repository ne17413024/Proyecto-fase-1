import os

productos = [
    ['juguetes', 'mono', 50, 'mona', 50, 'trampolin', 50, 'max-steel', 50],
    ['libros', 'libro1', 50, 'libro2', 50, 'libro3', 50, 'libro4', 50],
    ['comida', 'manzana', 5, 'banana', 3, 'pan', 2, 'leche', 4],
    ['ropa', 'camiseta', 20, 'pantalones', 30, 'chaqueta', 50, 'zapatos', 40]
]

productos_vendidos = []
total = 0.0

def venta():
    global productos_vendidos, total
    os.system("clear")
    print("\nCategorías y productos disponibles:")
    

    for categoria in productos:
        categoria_nombre = categoria[0]
        print(f"\nCategoría: {categoria_nombre}")
        
      
        print("Productos:")
        for i in range(1, len(categoria), 2):  
            producto = categoria[i]
            precio = categoria[i + 1]
            print(f"  - {producto}: ${precio}")
    
    print("\nIngresa los productos a vender uno por uno (ingresa '*' para salir):")
    
    estado = True
    productos_vendidos = []  
    total1 = 0.0  
    
    while estado:
        producto_vender = input("Producto a vender: ")
        
        if producto_vender == "*":
            estado = False
        else:
            encontrado = False
            for categoria in productos:
                for i in range(1, len(categoria), 2):  
                    if categoria[i] == producto_vender:
                        precio = categoria[i + 1]
                        productos_vendidos.append((producto_vender, precio))
                        total += precio
                        print(f"Producto '{producto_vender}' añadido a la venta con precio ${precio}.")
                        encontrado = True
                        break
                if encontrado:
                    break
            
            if not encontrado:
                print(f"Producto '{producto_vender}' no encontrado.")
    
    print("\nProductos vendidos:")
    for producto, precio in productos_vendidos:
        print(f"  - {producto}: ${precio}")
    
    print(f"\nTotal de la venta: ${total:.2f}")

def registrar_productos():
    os.system("clear")
    print("\nRegistrar productos. Categorías disponibles:")
    
    for i in range(0, len(productos)):
        print(productos[i][0])

    categoria_input = input("Categoría del producto: ")
    

    categoria_encontrada = False
    for categoria_actual in productos:
        if categoria_actual[0] == categoria_input:
            categoria_encontrada = True
            categoria_sublista = categoria_actual
            break

    if categoria_encontrada:
        producto = input("Producto a agregar: ")
        precio = float(input("Precio de este: "))
        
        # Agregar el nuevo producto
        categoria_sublista.append(producto)
        categoria_sublista.append(precio)
        
        print(f"Producto '{producto}' agregado a la categoría '{categoria_input}' con precio {precio}.")
    else:
        print(f"Categoría '{categoria_input}' no encontrada. Producto no registrado.")
        
def cierre():
    os.system("clear")
    print("Cierre")

    if productos_vendidos:
        print("\nResumen de productos vendidos:")
        for producto, precio in productos_vendidos:
            print(f"  - {producto}: ${precio}")
        
        print(f"\nTotal acumulado de ventas: ${total:.2f}")
    else:
        print("No se realizaron ventas.")

while True:
    print("\n1. Nueva venta")
    print("2. Registrar productos")
    print("3. Corte")

    seleccion = input("Selección: ")
    if seleccion == "1":
        venta()
    elif seleccion == "2":
        registrar_productos()
    elif seleccion == "3":
        cierre()
    elif seleccion == "*":
        print("Adios")
        break
    else:
        print("Seleccionaste una opción no válida.")