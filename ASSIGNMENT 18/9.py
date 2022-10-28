# 9. Write a python program to merge two python dictionaries into one dictionary.
d1={1:"ram",2:"nitu"}
d2={3:"nilu",4:"pillu"}

d1.update(d2)
del d2
print(d1)