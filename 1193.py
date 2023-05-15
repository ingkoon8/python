num = int(input())
c=1
a=0
d=1
while a<num:
    a+=1*c
    c+=1
    d+=1
    d%=2

if d == 1:
    row=a-num+1
    col=c-row

else:
    col = a-num+1
    row = c-col

print('{0}/{1}'.format(col,row))

