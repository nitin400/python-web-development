# 10. Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=int(input("Enter the third number"))
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
elif x==y:
    print(x)
elif x==z:
    print(z)
else:
    print(z)