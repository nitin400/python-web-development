# 8. Write a python script to print first N terms of a Fibonacci series
a=0
b=1
n=int(input("Enter how much terms you want"))
print(a,b,end=' ')
while(n):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    n-=1

