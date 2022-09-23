# 7. Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter the value of n"))
i=1

while(n>=i):
    if n%2==0:
        
        print(n)
    n=n-i