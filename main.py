# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:05:40 2022

@author: agata
"""

from klasy import zad_1 as z1
from klasy import zad_2 as z2
from klasy import zad_3 as z3


student1 = z1.Student("ania", [50, 40, 60, 60, 70, 80, 100])
print(student1.is_passed())

student2 = z1.Student("basia", [30, 40, 60, 20, 40, 35, 15])
print(student2.is_passed())

biblioteka1 = z2.Library('latowice', 'zielona',
                         '40-150', '8:00-16:00', '123123123')
biblioteka2 = z2.Library('zory', 'niebieska',
                         '30-120', '8:00-16:00', '321321321')

pracownik1 = z2.Employee('agata', 'krzykala', '10.10.2022',
                         '10.08.2000', 'katowice', 'czerwona',
                         '40-250', '234234234')
pracownik2 = z2.Employee('jakub', 'marzec', '15.09.2022',
                         '01.03.2000', 'jastrzebie', 'pszyczynska',
                         '33-222', '765432143')
pracownik3 = z2.Employee('jan', 'nowak', '08.08.2022',
                         '10.08.2002', 'zory', 'zorska',
                         '44-444', '987987987')

ksiazka1 = z2.Book(biblioteka1, '20.04.2017', 'Janina', "Nowakowa", '303')
ksiazka2 = z2.Book(biblioteka2, '13.76.2019', 'Janina', "Kowalska", '201')
ksiazka3 = z2.Book(biblioteka1, '15.06.2020', 'Mariusz', 'Pudzianowski', '404')
ksiazka4 = z2.Book(biblioteka2, '13.09.2021', 'Kacper', 'Chudy', '201')
ksiazka5 = z2.Book(biblioteka1, '11.11.2011', 'Ida', 'Lipa', '130')

student1 = z2.Student('123123')
student2 = z2.Student('123345')
student3 = z2.Student('123789')

zamowienie1 = z2.Order(pracownik3, student1, [ksiazka1, ksiazka2],
                       "15.10.2022")
zamowienie2 = z2.Order(pracownik2, student2,
                       [ksiazka2, ksiazka4, ksiazka5], "16.10.2022")

print(zamowienie2)

home1 = z3.Home(110, 6, 500000, 'debowa 12/3 katowice', 1000)
print(home1)

flat1 = z3.Flat(54, 3, 30000, 'wladyslawa lokietka 3/5 katowice', 3)
print(flat1)
