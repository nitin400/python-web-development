# 2. Write a Python script to create a list of first N odd natural numbers.
n=int(input("Enter the number"))
l1=[]
for i in range(1,n+1):
    if(i%2!=0):
        l1.append(i)
print(l1)