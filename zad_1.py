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


student1 = Student("ania", [50, 40, 60, 60, 70, 80, 100])
student1.is_passed()

student2 = Student("basia", [30, 40, 60, 20, 40, 35, 15])
student2.is_passed()
