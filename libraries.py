import math
import csv
import matplotlib
import selenium

def math_excercise():
    sqrt_table=[]
    for i in range (1,101):
        squarval=math.sqrt(i)
        sqrt_table.append(squarval)
        return sqrt_table

math_excercise()
