# 5. Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter the number"))
i=0
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)