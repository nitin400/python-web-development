f=open('test.txt','w')
f.write("Be a good listner")
f.close()

with open('test.txt','w') as f:
    f.write("Be a good listner")