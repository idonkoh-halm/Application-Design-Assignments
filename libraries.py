import math
import csv
import matplotlib
import selenium

def math_excercise():
    sqrt_table=[]
    for i in range (1,101):
        squarval=math.sqrt(i)
        sqrt_table.append([squarval])
    print sqrt_table    

#math_excercise()

def csv_excercise():
    with open('sqrttable.csv','a') as csvfile:
        squarereader=csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in squarereader:
              print ', '.join(row)

#with file ('sqrtables.csv','w'):
    
#csv_excercise()

from selenium import webdriver

driver=webdriver.Firefox()
driver.get('https://comeonandsl.am/')
