# 3. Write a python script to calculate sum of cubes of first N natural numbers

n=int(input("Enter the number"))
i=0
sum=0
while(i<=n):
    sum=sum+i*i*i
    i=i+1
print(sum)