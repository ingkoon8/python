num1, num2 = map(int,input().split())
save=[]
while num1!=0:
    if num1%num2 >= 10:
        save.append(chr((num1%num2)+55))
    else:
        save.append(num1%num2)    
    num1=num1//num2
        
save.reverse()
for i in save:
    print(i,end='')
