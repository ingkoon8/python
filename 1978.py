num = int(input())
a=[]
numf=[]
a=list(map(int,input().split()))
for i in range(num):
    com = int(a[i])
    cnt=0
    if com == 1:
        continue
    for j in range(1, com):
        if(com%j == 0):
            cnt+=1
        if j == (com-1):
            if cnt == 1:
                numf.append(com)

print(len(numf))
