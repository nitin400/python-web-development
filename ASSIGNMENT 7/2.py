# Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division
x=(input("Enter which operation you want to do"))
match x:
    case 'add':
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print(a+b)
    case 'substract':
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print(a-b)
    case 'multiply':
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print(a*b)
    case 'divide':
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print(a/b)
        
        
         
