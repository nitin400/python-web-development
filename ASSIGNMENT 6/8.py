# 8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots
a=int(input("Enter the value of a in the equation"))
b=int(input("Enter the value of b in the equation"))
c=int(input("Enter the value of c in the equation"))
d=(b**2)-4*a*c
if d<0:
    print("UNEQUAL AND IMAGINARY")  
elif d==0:
    print("REAL AND EQUAL")
else:
    print("REAL AND UNEQUAL")
