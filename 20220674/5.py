#program which reads 3 number and arrange them in ascending order.

x=int(input("enter the first no:"))
y=int(input("enter the second no:"))
z=int(input("enter the third no:"))

min=0
mid=0
max=0

if (x<y and x<z):
    if(y<z):
       min,mid,max=x,y,z
    else:
       min,mid,max=x,z,y
elif (y<x and y<z):
    if(x<z):
        min,mid,max=y,x,z
    else:
         min,mid,max=y,z,x
else: 
    if (x<y):
        min,mid,max=z,x,y
    else:
        min,mid,max=z,y,x

print("ascending order of our input %d,%d,%d"%(min,mid,max))           

