# 9. Write a python script to check whether a given year is a leap year or not.
x=int(input("Enter the year"))
if x%4 or x%400:
    print("it is leap year")
else:
    print("It is not leap year")