"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Assignment 1, Module 1, Task 4
"""
from statistics import mean as mn
import math

#Variable declaration: single list, integer for while loops
mylist = []
i = 1
j = 0

#Loop to place input from user into list
while i < 4:
    x = int(input("Enter a City Population :"))
    mylist.append(x)
    i += 1

# Part 3 Check Values
while j < 3: 
    if (mylist[j] < 0) :
        print("A City cannot have a negative population")
        x = int(input("Enter a City Population :"))
        mylist.pop(j)
        mylist.insert(j,x)

    if (mylist[j] == 0) :
        print("A City must have at least 1 person living in it")
        x = int(input("Enter a City Population :"))
        mylist.pop(j)
        mylist.insert(j,x)

    if (mylist[j] > 70000000000000) :
        print("Not Everyone can Live in the Same City!")
        x = int(input("Enter a City Population :"))
        mylist.pop(j)
        mylist.insert(j,x)
    j += 1

# Sum of all popultion inputs
sum = sum(mylist)   
print("The Sum of the total population is : ", sum) 

#The Average of all population inputs
avg = round(mn(mylist))
print("The Average of all the populations is: ", avg)

#The product of all the population inputs
prod = math.prod(mylist)
print("The Product of all the populations is: ", prod)

#The Minimum value of the given list
smallest = min(mylist)
print("The Smallest Popultion is: ", smallest)

#The maximum value of the given list
biggest = max(mylist)
print("The Largest population is: ", biggest)

#The range of populations of the given list
print("The Range of the population is: ", smallest, " - ", biggest)

