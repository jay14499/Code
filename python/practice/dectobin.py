x=int(input("enter the value: "))
base=1
s=0
for x in range (x//2):
    if x>0:
        y=x%2
        s=s+y*base 
        base=base*10
       # x=x/2
    else:
        print(s)
print(s)  