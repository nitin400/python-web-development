# 4. Write a python script to print first N odd natural numbers

n=int(input("Enter the value of n"))
i=1

while(i<=n):
    if i%2!=0:
        
        print(i)
    i=i+1