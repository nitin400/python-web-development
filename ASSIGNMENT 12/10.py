# 10. Write a python script to calculate HCF of two numbers
a,b=(int(input("Enter first number"))),(int(input("Enter second number")))
n=[]
for i in range(2,a*b):
    if(a%i==0 and b%i==0):
        n.append(i)
        i=i*2
print(max(n))