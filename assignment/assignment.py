#program to make dictonery of team and their wins and losses

#from ast import Break
#from bdb import Breakpoint
#from lib2to3.pgen2.token import PERCENT


d={}
n=int(input("enter the number teams participated: "))

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