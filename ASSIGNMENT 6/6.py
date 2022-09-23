# 6. Write a python script to check whether a given number is a three digit number or not.
x=int(input("Enter the number"))
count=0
while(x):
    
    count=count+1
    x=x//10

print(count)