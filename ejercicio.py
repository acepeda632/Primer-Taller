import csv
import json

def ejercicio():
    # Leer los datos:
    with open('data.json', 'r', encoding='utf-8') as file:
        usuarios = json.load(file)

    # 1. Gasto total por usuario:
    gastos_totales = {}
    for usuario in usuarios:
        total = 0
        for compra in usuarios[usuario]:
            total = total + compra['precio']
        gastos_totales[usuario] = total

    print("1. Gasto total por usuario:")
    for usuario in gastos_totales:
        print(f"{usuario}: {gastos_totales[usuario]:.2f} €")

    # 2. Clientes VIP.
    clientes_vip = max(gastos_totales, key=gastos_totales.get)
    print(f"\n2. Cliente VIP: {clientes_vip} con un gasto total de {gastos_totales[clientes_vip]:.2f} €")

    # 3. Clientes con más artículos.
    articulos_totales = {}
    for usuario in usuarios:
        articulos_totales[usuario] = len(usuarios[usuario])
    
    mas_articulos = max(articulos_totales, key=articulos_totales.get)
    print(f"\n3. Cliente con más artículos: {mas_articulos} con {articulos_totales[mas_articulos]} artículos")

    # 4. Producto más caro y más barato.
    todas_compras = []
    for usuario in usuarios:
        for compra in usuarios[usuario]:
            todas_compras.append((compra, usuario))

    caro, comprador_caro = todas_compras[0]
    barato, comprador_barato = todas_compras[0]
    for compra, usuario in todas_compras:
        if compra['precio'] > caro['precio']:
            caro = compra
            comprador_caro = usuario
        if compra['precio'] < barato['precio']:
            barato = compra
            comprador_barato = usuario  

    print(f"\n4. Producto más caro: {caro['producto']} de {caro['precio']} € comprado por {comprador_caro}")
    print(f"Producto más barato: {barato['producto']} de {barato['precio']} € comprado por {comprador_barato}")

    # 5. Resumen por categorías.
    categorias = {}
    for compra, usuario in todas_compras:
        categoria = compra['categoria']
        if categoria in categorias:
            categorias[categoria] += compra['precio'] 
        else:
            categorias[categoria] = compra['precio']

    for categoria, total in categorias.items():
        categorias[categoria] = round(categorias[categoria], 2)

    print(f"\n5. Resumen por categorías: {categorias}")

    # 6. Añadir precios con IVA a cada compra.
    for usuario in usuarios:
        for compra in usuarios[usuario]:
            compra['precioIVA'] = round(compra['precio'] * 1.21, 2)

    # 7. Crear el CSV con producto y precios IVA:
    with open("ejercicio.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["producto", "precioIVA"])
        for usuario in usuarios:
            for compra in usuarios[usuario]:
                writer.writerow([compra['producto'], compra['precioIVA']])

    print()
    print("7. CSV creado: ejercicio.csv")

if __name__ == "__main__":
    ejercicio()