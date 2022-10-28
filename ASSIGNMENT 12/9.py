# 9. Write a python script to calculate LCM of two numbers
a,b=(int(input("Enter first number"))),(int(input("Enter second number")))

for i in range(2,a*b):
    if(a%i==0 and b%i==0):
        print(i)
        break