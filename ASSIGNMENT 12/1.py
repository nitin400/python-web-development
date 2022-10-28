# 1. Write a python script to reverse a number
n=int(input("Enter the number"))
while(n>0):
    first=n%10
    n=n//10
    x=first
    print(x,end="")