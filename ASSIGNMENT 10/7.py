# 7. Write a python script to print first N odd natural numbers

n=int(input("Enter how much natural numbers you want"))

for x in range(1,2*n):
    if(x%2):
        print(x)