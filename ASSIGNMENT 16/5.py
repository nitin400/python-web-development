# 5. Write a python program to check if all items in the tuple are the same

t=(1,1,1,1,1,1)
count=0
for i in t:
    if(t[i]==1):
        count+=1
        if(count==6):
            print("SAME")
    else:
        print("not same")