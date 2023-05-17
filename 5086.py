import sys
c=[]
try:
    while 1:
        num1, num2 = map(int,sys.stdin.readline().split())
        a=num2//num1
        b=num2%num1
        if(a==0 and b != 0 ):
            if num1//num2 != 0 and num1 % num2 == 0:
                c.append('multiple')
            else:
                c.append('neither')
        elif(a!=0 and b == 0):
            c.append('factor')
        else:
            c.append('neither')

except ZeroDivisionError:
    pass

for i in c:
    print(i)
