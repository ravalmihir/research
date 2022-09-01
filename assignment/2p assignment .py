#program to find statistical data of string.
#  it is a intresting program for me beacuse i love the output of this program
# which gives  calculation of uppercase,lowercase,digit,othercase,spaces.
string = input("enter the string here:")
uppercase=0
lowercase=0
digit=0
othercase,spaces=0
#using for hear to put a in string.
#using if else statement for performing logic inside.
for a in string:
    if(a.isupper()):
        uppercase+=1
    elif(a.islower()):
        lowercase+=1
    elif(a.isdigit()):
        digit+=1
    else:
        othercase,spaces+=1

print("number of uppercase letter are:",uppercase)     
print("number of lowercase letter are:",lowercase)     
print("number of digit letter are:",digit)     
print("number of othercase and spaces are:",othercase,spaces)       
