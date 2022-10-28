# 4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)
min=int(input("Enter the minimum limit"))
max=int(input("Enter the maximum limit"))
for number in range(min,max+1):
    count=0
    for i in range(2,(number//2)):
        if(number%i==0):
            count=count+1
            break
    if (count == 0 and number != 1):
        print(" %d" %number, end = '  ')
    