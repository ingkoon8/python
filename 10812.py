import sys

basket, turn = map(int, input().split())
a=[]
b=[]
c=[]

for i in range(basket):
    a.append(i+1)
for i in range(turn):
    begin, end, mid = map(int, sys.stdin.readline().split())
    for j in range(end+1-begin):
        n=mid-begin
        b=a[begin-1:end]
        if j+n<len(b):
            c.append(b[j+n])
        else:
            c.append(b[j+n-len(b)])
    a=a[:begin-1]+c+a[end:]
    c.clear()
for i in a:
    print(i, end=' ')
