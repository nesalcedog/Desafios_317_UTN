## Desafio 1) ##

altura = int(input("Ingrese la altura del jugador: "))

if altura < 160:
    print("La posición del jugador es Base")
elif 160 <= altura <= 179:
    print("La posición del jugador es Escolta")
elif 180 < altura <= 199:
    print("La posición del jugador es Alero")
else:
    print("La posición del jugador es Ala-Pivot o Pivot")


## Desafio 1) mejorado ##

altura = int(input("Ingrese la altura del jugador en cm: "))

if altura < 160:
    print("La posición del jugador es Base")
elif altura <= 179:
    print("La posición del jugador es Escolta")
elif altura <= 199:
    print("La posición del jugador es Alero")
else:
    print("La posición del jugador es Ala-Pivot o Pivot")


## Desafio 2) ##

# nota = int (input("Ingrese su nota: "))

# if nota > 10:
#     print(f"Nota ingresada incorrecta")
# else:
#     if 5 < nota <= 10:
#         print(f"Promoción directa, la nota es", nota)
#     elif nota == 4 or nota == 5:
#         print(f"Aprobado, la nota es", nota)
#     else:
#         print(f"Desaprobado, la nota es", nota)

    