A,B,V=map(int,input().split())
V=V-A
h=A-B
day=V//h
if V%h != 0:
    day+=1
print(day+1)
