producto = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', 'IT', 'Intel Core i5', 'Nvidia GTX1050', 800],
    '2175HD': ['Lenovo', 14, '16GB', 'SDD', '512GB', 'Intel Core i5', 'Nvidia GTX1050', 900],
    'jJFHDD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti', 600],
    'fgdxFDH': ['HP', 15.6, '8GB', 'IT', 'Intel Core i3', 'integrada', 1000],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', 'IT', 'Intel Core i7', 'Nvidia GTX1050', 1500],
    '123FDH': ['Lenovo', 14, '6GB', 'DD', 'IT', 'AMD Ryzen 5', 'integrada', 2500],
    '342FDH': ['Lenovo', 15.6, '8GB', 'IT', 'AMD Ryzen 7', 'Nvidia GTX1050', 1800],
    'UWU131HD': ['Dell', 15.6, '8GB', 'IT', 'AMD Ryzen 3', 'Nvidia GTX1050', 2800],
}

inventario = {
    '8475HD': [10, 4],
    '2175HD': [5, 2],
    'jJFHDD': [8, 3],
    'fgdxFDH': [12, 7],
    'GF75HD': [6, 0],
    '123FDH': [9, 1],
    '342FDH': [7, 3],
    'UWU131HD': [10, 5]
}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = 0
    for prod_id, datos in producto.items():
        if datos[0].lower() == marca:
            if prod_id in inventario:
                total_stock += inventario[prod_id][1]
    return total_stock

def busqueda_por_precio(min_precio, max_precio):
    resultados = []
    for prod_id, datos in producto.items():
        precio = datos[-1]
        if min_precio <= precio <= max_precio and inventario[prod_id][1] > 0:
            resultados.append(f"{prod_id} - {datos[0]} - ${precio}")
    return sorted(resultados)

def actualizar_stock(prod_id, nueva_cantidad):
    if prod_id in inventario:
        inventario[prod_id][1] = nueva_cantidad
        return True
    return False

def actualizar_precio(prod_id, nuevo_precio):
    if prod_id in producto:
        producto[prod_id][-1] = nuevo_precio
        return True
    return False

def menu():
    while True:
        print("\n*** MENURINCIPAL ***")
        print("1. Consultar stock por marca")
        print("2. Buscar por precio")
        print("3. Actualizar precio")
        print("4. Salir")

        opcion = input("Ingrese opcion ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            total = stock_marca(marca)
            print(f"El stock disponible para {marca.capitalize()} es: {total}")

        elif opcion == '2':
            try:
                min_precio = float(input("Ingrese precio minimo"))
                max_precio = float(input("Ingrese precio maximo"))
                resultados = busqueda_por_precio(min_precio, max_precio)
                if resultados:
                    print("PC encontrados en ese precio:")
                    for r in resultados:
                        print(f" - {r}")
                else:
                    print("No se encontraron PC en ese rango de precio")
            except ValueError:
                print("Debe ingresar valores enteros")

        elif opcion == '3':
            prod_id = input("Ingrese ID del producto para actualizar precio: ").strip()
            if prod_id not in producto:
                print("ID no encontrado en productos.")
                continue
            nuevo_precio = input("Ingrese nuevo precio: ").strip()
            try:
                nuevo_precio = float(nuevo_precio)
                if actualizar_precio(prod_id, nuevo_precio):
                    print(f"Precio actualizado para {prod_id}: ${nuevo_precio}")
                else:
                    print("Error al actualizar el precio.")
            except ValueError:
                print("Precio inválido. Debe ser un numero")

        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Debe Seleccionar una opcion Valida!!")
