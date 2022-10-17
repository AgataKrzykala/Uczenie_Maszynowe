# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:42:52 2022

@author: agata
"""


def funkcjaA(lista):
    for imie in lista:
        print(imie)


funkcjaA(['Ania', "Kasia", 'Basia', "Jasia", 'Asia'])


def funkcjaBfor(liczby):
    for i in range(len(liczby)):
        liczby[i] = liczby[i]*2
    return liczby


print(funkcjaBfor([1, 2, 3, 4, 5]))


def funkcjaBlistaSkladana(liczby):
    liczby2 = [2*x for x in liczby]
    return liczby2


print(funkcjaBlistaSkladana([5, 4, 3, 2, 1]))


def funkcjaC(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)


funkcjaC([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


def funkcjaD(lista):
    for i in lista[::2]:
        print(i)


funkcjaD([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])
