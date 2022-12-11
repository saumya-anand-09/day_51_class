f= open("demo1.txt","r")
print(f.readlines())
print(f)
print(f.name)
#func to read the lkines from a text file and display the words which are having less than 4 four char.


f1= int(input("Enter: "))
f2= int(input("Enter: "))
try:
    f1/f2
except:
   print("error")
else:
    print("a number cannot be divided by zero")
finally:
    print("program executed")


 #finally has more priority

for x in range(2, 6):
  print(x)

i = -77
while i>88:
    print(i)
    if i ==88:
        break
    i+=1   
