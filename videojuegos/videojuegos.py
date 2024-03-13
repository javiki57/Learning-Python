#!/usr/bin/env python3

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]
tope = 100

# Géneros
generos = {
    "Super Mario Bros" : "Aventura",
    "Zelda: Breath of the Wild" : "Aventura",
    "Cyberpunk 2077" : "Role",
    "Final Fantasy VII" : "Role"
}

# Ventas y Stock
ventas_y_stock ={
    "Super Mario Bros" : (400, 200),
    "Zelda: Breath of the Wild" : (600, 20),
    "Cyberpunk 2077" : (60, 120),
    "Final Fantasy VII" : (924, 3)
}

# Clientes
clientes = {    
    "Super Mario Bros" : {"Marcelo", "Hackermate", "Lobotec", "Diego", "Roberto"},
    "Zelda: Breath of the Wild" : {"Lucía", "Manolo", "Carlos", "María", "Timmy"},
    "Cyberpunk 2077" : {"Lobotec", "Raquel", "Pepe", "Carolina", "Álex"},
    "Final Fantasy VII" : {"Lucía", "Manolo", "Pepe", "Securiters", "Patricia", "Moisés"}
}

def sumario(juego):
    # Sumario
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

total_ventas = lambda: sum(ventas for juego, (ventas,_) in ventas_y_stock.items() if ventas > tope) # La _ quiere decir que lo que sea, ya que no me interesa ese elemento

print(f"\nLas ventas totales de juegos han sido {total_ventas()}")    # Como es una función lambda hay que poner total_ventas()
