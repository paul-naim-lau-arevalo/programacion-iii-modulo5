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

nombre = input("Ingresa un nombre: ")

if nombre in edades:
    print(f"{nombre} tiene {edades[nombre]} años.")
else:
    print("La persona no fue encontrada.")
