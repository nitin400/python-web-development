# 3. Write a python script to print all Prime numbers under 100
for number in range(1,101):
    count=0
    for i in range(2,(number//2)):
        if(number%i==0):
            count=count+1
            break
    if (count == 0 and number != 1):
        print(" %d" %number, end = '  ')
    
