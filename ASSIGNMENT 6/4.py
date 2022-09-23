# 4. Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
if x>y:
    print("x is greater number",x)
elif x==y:
    print(x)
else:
    print("y is greater number",y)
