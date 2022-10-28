# 9. Write a Python script to create a list of city names taken from the user.
n=eval(input("How many citites do you want to insert"))
city=eval(input("Enter the city names "))
l1=[]

for i in range(n):
    l1.append(city[i])
print(l1)