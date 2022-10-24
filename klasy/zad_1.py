# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:35:38 2022

@author: agata
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if (sum(self.marks)/len(self.marks) > 50):
            return True
        else:
            return False
