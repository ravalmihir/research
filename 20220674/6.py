#program that print the factor of any number.
# it is small program but helpfull in mathematics.
#easily know the factor of any number.

num=int(input("enter the any no: "))
print("the factor of ",num,"are: ")
for a in range(1,num+1):
    rem=num%a
    if(rem==0):
      print(a)
 
