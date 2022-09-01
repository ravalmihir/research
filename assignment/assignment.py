#program to make dictonery of 2 teams and their wins and losses and gives winning percentage of team which you entered in output.

#from ast import Break
#from bdb import Breakpoint
#from lib2to3.pgen2.token import PERCENT

#it is intresting program although i felt difficulties in the logic of this program.
#when i spend hours in the code then i got perfect output.
d={}
n=int(input("enter the number teams participated: "))

#this code is done by for loop and if else statement

for a in (0,n):
    tname=input("enter the team name:")
    won=int(input("enter the games won: "))
    lost=int(input("enter the games lost: "))
    l=[won,lost]
    d[tname]=l
    print(d)

t = input("enter the name of team from above dictionary: ")

if t in d:
     tgames=d[t][0]+d[t][1]
     PERCENT = d[t][0]/tgames*100
     print(PERCENT,"is winning percent of the team")
else:
    print("you enter a wrong team name ")  
    #code is ready
    #this code is use in sports and games area.
