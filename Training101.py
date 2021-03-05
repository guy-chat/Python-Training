# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 01:46:25 2020

@author: Bhumipat Chatlekhavanich
https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""

"""
#Exercise 1
#\t is indent \n is new line \ alone can continue the print to next line
print("Twinkle, twinkle little star, \n\tHow I wonder what you are!\n\t\tUp \
above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, \
little star,\n\tHow I wonder what you are")


#Exercise 2 - get python version
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

#Exercise 3 - Display current date and time
import time
print("Current date and time : ")
print(time.strftime("%Y-%m-%d %H:%M:%S"))

#Exercise 4 - function that takes radius val and output area of circle
from math import pi
r = float(input("Radius value : "))
print("Area of circle with rad "+ str(r) + "equals to " +str(pi*r**2))

#Ex 5 - input name and put in reverse
X = str(input("First name : "))
Y = str(input("Last name : "))
print(Y + " " + X)

#Ex 6 - turns inputs into lists and tuples
Values = input("Data (lists of number with , in between) : ")
List = Values.split(",")
Tuple = tuple(List)
print("List :" + str(List))
print("Tuple :" + str(Tuple))

#Ex 7 - input file name output file type
File_name = input("File name : ")
Filename_str = File_name.split(".")
print(str(Filename_str[-1]))

#Ex 8 - display the first and last of this list
color_list = ["red","green","white","black"]
print(color_list[0] +" "+ color_list[-1])

#Ex 9 - extract info from a list into desired form
exam_st_date = (11,12,2014)
print("The examination will start from : "+str(exam_st_date[0])+"/"+str(exam_st_date[1])+"/"+str(exam_st_date[2]))

#Ex 10 - input n, output = n+nn+nnn
n = input("n is : ")
sum_n = int(n)+int(n+n)+int(n+n+n)
print(sum_n)
"""
#Ex 11 - 

name = input('What is your name?\n')
print('Hi, %s.' % name)
print('i need to know if this is going to work')

