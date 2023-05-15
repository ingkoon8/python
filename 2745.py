num1, num2 = map(list,input().split())
num1.reverse()
num2=int(''.join(num2))
save=0
for i in range(len(num1)):
    try:
        save+=(int(num1[i])*(num2**i))
    except:
        save+=(ord(num1[i])-55)*(num2**i)
print(save)
