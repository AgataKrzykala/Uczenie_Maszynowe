# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:38:09 2022

@author: agata
"""
# 1


def funkcja(name: str, surname: str) -> str:
    string = f"Czesc {name} {surname}!"
    return string


text = funkcja("agata", "krzykała")
print(text)

# 2


def funkcja2(a: int, b: int):
    return a * b


print(funkcja2(1, 4))

# 3


def funkcja3(a: int) -> bool:
    if a % 2 == 0:
        return True
    else:
        return False


wynik = funkcja3(5)
if wynik is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# 4


def funkcja4(a: int, b: int, c: int) -> bool:
    if (a + b >= c):
        return True
    else:
        return False


print(funkcja4(1, 2, 5))

# 5


def funkcja5(lista: list, a: int) -> bool:
    if a in lista:
        return True
    else:
        return False


print(funkcja5([1, 2, 3], 5))

# 6


def funkcja6(a: list, b: list) -> list:
    lista = a + b
    lista = [x**3 for x in lista]
    lista = list(dict.fromkeys(lista))
    return lista


print(funkcja6([1, 2, 2, 3, 3, 4, 5], [1, 2, 6, 7, 7, 8]))
