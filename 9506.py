import sys
fac=[]
sum=0
num2=[]

while 1:
    num1 = int(sys.stdin.readline())
    if(num1==-1):
        break
    num2.append(num1)

for num in num2:    
    for i in range(1, num):
        if(num%i==0):
            fac.append(i)
            sum+=i
    if sum == num:
        print('{0} ='.format(num),end=' ')
        for i in fac:
            if(i != fac[-1]):
                print('{0} +'.format(i),end=' ')
            else:
                print(i)
    else:
        print('{0} is NOT perfect.'.format(num))
    fac.clear()
    sum=0

        
