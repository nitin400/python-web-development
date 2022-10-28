# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
# "Python", "Django"}

thisset = {"Java", "Python", "Django"}
for i in thisset:
    if("Python" in thisset):
        print("present")
        break
    else:
        print("not present")