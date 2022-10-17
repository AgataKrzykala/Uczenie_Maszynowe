# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:51:48 2022

@author: agata
"""


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class Home(Property):
    def __init__(self, area, rooms, price, address, plot):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.plot = plot

    def __str__(self):
        return f"""powierzchnia: {self.area}, pokoje: {self.rooms},
    cena: {self.price}, adres: {self.address},
    rozmiar dzialki: {self.plot}"""


class Flat(Property):

    def __init__(self, area, rooms, price, address, floor):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.floor = floor

    def __str__(self):
        return f"""powierzchnia: {self.area}, pokoje: {self.rooms},
    cena: {self.price}, adres: {self.address},
    pietro: {self.floor}"""


home1 = Home(110, 6, 500000, 'debowa 12/3 katowice', 1000)
print(home1)

flat1 = Flat(54, 3, 30000, 'wladyslawa lokietka 3/5 katowice', 3)
print(flat1)
