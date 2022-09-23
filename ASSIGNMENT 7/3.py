# Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
from tkinter import N


print(" 1- check whether three numbers are lengths of an isosceles triangle or not \n 2- check whether a given set of three number are length of sides of a right angled triangle or not\n 3- for equilaterial triangle")
x=int(input())
match x:
    case 3:
        x=int(input("Enter the lenths of the triangles"))
        y=int(input("Enter the lenths of the triangles"))
        z=int(input("Enter the lenths of the triangles"))
        if x==y==z:
            print("triangle is equilaterial")
        else:
            print("NOT equilaterial")
    case 2:
        x=int(input("Enter the lenths of the triangles"))
        y=int(input("Enter the lenths of the triangles"))
        z=int(input("Enter the lenths of the triangles"))
        
        if z**2==x**2+y**2:
            print("It is a right angled triangle")
        else:
            print("Not equilaterial")
    case 1:
        x=int(input("Enter the lenths of the triangles"))
        y=int(input("Enter the lenths of the triangles"))
        z=int(input("Enter the lenths of the triangles"))
        if x==y or y==z:
            print("It is isoceles triangle")
        else:
            print("Not isoceles")