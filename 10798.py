b=[]
for i in range(5):
    b.append(input())

for i in range(15):
    for j in range(5):
        try:
            print(b[j][i],end='')
        except:
            print('',end='')
