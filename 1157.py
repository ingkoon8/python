string = input()
a={}
b=[]
for i in range(26):
    count = string.count(chr(97+i)) + string.count(chr(65+i))
    if a.get(count) == None:
        a.setdefault(count,chr(65+i))
    else:
        b.append(a.get(count))
max=max(a)
try:
    b.index(a.get(max))
    print('?')
except:
    print(a.get(max))
