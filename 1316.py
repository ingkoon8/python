import sys
num = int(input())
b=[]
a=0
for i in range(num):
    string=sys.stdin.readline()
    for j in range(len(string)):
        if j == 0:
            b.append(string[j])
            continue
        if string[j]==string[j-1]:
            continue
        else:
            if b.count(string[j]) != 0:
                break
            else:
                b.append(string[j])
                if j==(len(string)-1):
                    a+=1       
    b.clear()
print(a)
