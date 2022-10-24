# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:55:20 2022

@author: agata
"""


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"""miasto: {self.city}, ulica: {self.street},
   kod pocztowy: {self.zip_code}, godziny otwarcia: {self.open_hours},
    numer telefonu: {self.phone}"""


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"""imie: {self.first_name}, nazwisko: {self.last_name},
    data zatrudnienia: {self.hire_date}, data urodzenia: {self.birth_date},
    miasto: {self.city}, ulica: {self.street}, kod pocztowy: {self.zip_code},
    numer telefonu: {self.phone}"""


class Book:
    def __init__(self, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"""biblioteka: {self.library},
    data publikacji: {self.publication_date},
  imie autora: {self.author_name},
  nazwisko autora: {self.author_surname},
    liczba stron: {self.number_of_pages}"""


class Student:
    def __init__(self, nr_albumu):
        self.nr_albumu = nr_albumu

    def __str__(self):
        return f'numer albumu: {self.nr_albumu}'


class Order():
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"""pracownik: {self.employee},
    \n student: {self.student},
    \n ksiazka: {self.books},
    \n data zamowienia: {self.order_date}\n"""
