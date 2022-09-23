# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
x=int(input("Enter the age "))
match x<10:
    case :
        print("kid")

match x>=10 and x<20:
    case 2:
        print("Teen")

match x>=20 and x<40:
    case 3:
        print("young")
match x>=40 and x<60:
    case 4:
        print("experienced")
match x>=60:
    case 5:
        print("Senior Citizen")