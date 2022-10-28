# 4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter the number"))
i=0
sum=0
while(i<=n):
    if(i%2):
        sum=sum+i
    i=i+1
print(sum)