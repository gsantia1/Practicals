""" Gauvan Santiago Prac 03 Task 02"""

import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)