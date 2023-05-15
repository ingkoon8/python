num1 = int(input())
coin = [25,10,5,1]
wallet1=[]
wallet2=[]
for i in range(num1):
    money = int(input())
    for j in coin:
        wallet1.append(money//j)
        money %= j     
    wallet2.append(wallet1)
    wallet1=[]

for i in range(num1):
    for j in wallet2[i]:
        print(j,end=' ')
    print()
