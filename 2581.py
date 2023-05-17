num1=int(input())
num2=int(input())
numf=[]
for i in range(num1,num2+1):
    if i == 1:
        continue
    if i == 2:
        numf.append(i)
    for j in range(2, i):
        if i%j == 0:
            break
        if j== i-1:
            numf.append(i)
            

if sum(numf) != 0:
    print(sum(numf))
    print(min(numf))
else:
    print(-1)
