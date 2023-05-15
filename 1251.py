str=list(input())
a=[]

for i in range(1,len(str)-1):
    for j in range(i+1,len(str)):
        str1=str[:i]
        str2=str[i:j]
        str3=str[j:]

        str1.reverse()
        str2.reverse()
        str3.reverse()
        
        a.append(''.join(str1+str2+str3))
print(min(a))
