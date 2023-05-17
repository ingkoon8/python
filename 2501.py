num1, num2 = map(int,input().split())
fac=[]

for i in range(1, num1+1):
    if(num1%i==0):
        fac.append(i)
try:
    print(fac[num2-1])
except:
    print(0)
