import sys
paper=[]
for i in range(101):
    paper.append([0]*101)
count=0
num=int(input())
for i in range(num):
    col, row = map(int,sys.stdin.readline().split())
    for j in range(col+1, col+11):
        for k in range(row+1, row+11):
            paper[j][k]+=1

for i in range(101):
    for j in range(101):
        if paper[i][j] != 0:
            count+=1

print(count)
