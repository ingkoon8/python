bee = int(input())
k=1
bee-=1
while 1:
    if bee==0:
        count=k
        break
    bee-=6*k
    if bee<=0:
        count = k+1
        break
    k+=1
   

print(count)
