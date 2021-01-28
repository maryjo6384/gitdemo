
#Demo to use for loop

#prints the values in list
val = [5,6,7,7,7]
dict ={"a":"1","b":"2"}

print(val)
print(*val)
print(*val,sep="")

for key,values in dict.items():
    print(values)

for i in val:
    print(i)

for i in range(0,len(val)):
    print (val[i])

for i in range(len(val)-1,0,-1):
    print(val[i])

for index,value in enumerate(val):
    print(val)
#prints the value in the string

str="Josephine"
for i in str:
    print(i)

#program to add first 5 natural numbers

total = 0
for i in range(1,6): #for i=0;i<6;i++
    total=i+total

print("Value of first 5 natural numbers",total)

#program to understand iterations

print("*************Program to understand iterations********")
for i in range(0,6):
    print ("This means range 0 to 6 ",i)

for j in range(0,10,2):
    print("This means range 0 to 10 with +2 iterations",j)

for k in range(10):
    print("This means range 10",k)