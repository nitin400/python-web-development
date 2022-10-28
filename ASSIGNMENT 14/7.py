
# 7. Write a Python script to remove all non int values from a list.

l1=[1,3,"nitin",5,8,"andhale"]
l2=[]
for i in l1:
    if(i in (1,3,5,8)):
        l2.append(i)
print(l2)