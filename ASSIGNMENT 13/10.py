# 10. Write a Python script to create a list, where each element of the list is a digit of a
# given number.
n=int(input("Enter the number"))
l1=[]
while(n):
    l1.append(n%10)
    n=n//10
l1.reverse()
print(l1)