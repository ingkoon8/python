col=0
row=0
matrix=[]
maxN=0
for i in range(9):
    matrix.append(list(map(int,input().split())))
    if maxN <= max(matrix[i]):
        maxN = max(matrix[i])
        col=i+1
        row=(matrix[i].index(maxN))+1

print(maxN)
print(col,row)
