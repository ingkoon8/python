string = input()
alphabet=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in alphabet:
    if string.count(i) != 0:
        string=string.replace(i,' ')
print(len(string))
