import math
import csv
import matplotlib
#import selenium

def math_excercise():
    sqrt_table=[]
    sqrt_table.append(["Square root","Number"])
    for i in range (1,101):
        squarval=math.sqrt(i)
        sqrt_table.append([squarval,i])
    print sqrt_table
    return sqrt_table

math_excercise()

def csv_excercise():
    with open('sqrttable.csv','w') as csvfile:
        squarewriter=csv.writer(csvfile)
        for row in math_excercise():
              squarewriter.writerow(row)

#with file ('sqrtables.csv','w'):
    
csv_excercise()

#from selenium import webdriver

#driver=webdriver.Firefox()
#driver.get('https://reddit.com/r/random/top/?sort=top&t=all')
