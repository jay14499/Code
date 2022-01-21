x=int(input("enter the value of x: "))
y=x//2
print(y)
flag=0
for i in range(2,y):
    if((x%i)==0):
       flag=1
       break
    else:
        flag=0
if(flag==1):
    print(x, "is not a prime number")
else:
    print(x,"is a prime number")