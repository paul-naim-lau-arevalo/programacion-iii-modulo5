# Taller grupal - Modulo 5
# Listas, diccionarios y condicionales

nombres = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]
edades = {
    "Ana": 30,
    "Luis": 25,
    "Carlos": 22,
    "Maria": 28,
    "Pedro": 35
}

while True:
    nombre = input("Ingresa un nombre (o 'salir' para terminar): ").strip().title()

    if nombre == "Salir":
        print("Programa finalizado.")
        break

    if nombre in edades:
        print(f"{nombre} tiene {edades[nombre]} años.")
    else:
        print("La persona no fue encontrada.")
