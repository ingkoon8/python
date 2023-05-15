col, row=map(int,input().split())
matrixA=[]
matrixB=[]

for i in range(col):
    matrixA.append(list(map(int,input().split())))
for i in range(col):
     matrixB.append(list(map(int,input().split())))

for i in range(col):
    for j in range(row):
        print(int(matrixA[i][j])+int(matrixB[i][j]), end=' ')
    print()
