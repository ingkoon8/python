string = input()
if len(string) == 1:
    print(1)

for i in range(int(len(string)/2)):
    if string[i]==string[-1-i]:
        pass
        if i+1==int(len(string)/2):
            print(1)
    else:
        print(0)
        break
