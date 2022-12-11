f  =open('helloi.txt','r')
z = f.read()
count = 0
for char in z:
    if(char =="a"):
        count+=1
print(count)        