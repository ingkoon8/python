case = int(input())
score=[]
for i in range(case):
    stuList = list(map(int,input().split()))
    save=0
    over=0
    for j in range(1, len(stuList)):
        save+=stuList[j]
        avg=save/stuList[0]
    for j in range(1, len(stuList)):
        if stuList[j] > avg:
            over+=1
    over=float(over/stuList[0]*100)
    score.append(over)

for i in score:
    print('%.3f%s' %(i,'%'))
