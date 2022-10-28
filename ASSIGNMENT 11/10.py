# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)
n=int(input("Enter the number"))
a=[]
while(n>0):
    dig=n%8
    a.append(dig)
    n=n//8
a.reverse()
for i in a:
    print(i,end=" ")
