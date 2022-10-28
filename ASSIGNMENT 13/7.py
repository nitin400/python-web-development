# 7. Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist=["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

for i in range(thislist.index(thislist[-1])+1):
    print(thislist[i])