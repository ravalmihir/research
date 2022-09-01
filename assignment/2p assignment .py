#program to find statistical data of string.

string = input("enter the string here:")
uppercase=0
lowercase=0
digit=0
othercase=0
#using for hear to put a in string.
#using if else loop for performing logic inside.
for a in string:
    if(a.isupper()):
        uppercase+=1
    elif(a.islower()):
        lowercase+=1
    elif(a.isdigit()):
        digit+=1
    else:
        othercase+=1

print("number of uppercase letter are:",uppercase)     
print("number of lowercase letter are:",lowercase)     
print("number of digit letter are:",digit)     
print("number of othercase and spaces are:",othercase)       
