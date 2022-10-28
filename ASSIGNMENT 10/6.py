# 6. Write a python script to print first N even natural numbers.

n=int(input("Enter how much natural numbers you want"))

for x in range(1,2*n):
    if(x%2==0):
        print(x)