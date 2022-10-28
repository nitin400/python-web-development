# 8. Write a python script to calculate sum of digits of a given number
n=int(input("Enter the number"))
i=0
x=0
sum=0
while(n>0):
    x=n%10
    sum=sum+x
    n=n//10
    
print(sum)