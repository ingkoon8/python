import sys
score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
a=0
b=0
for i in range(20):
    student=sys.stdin.readline().split()
    if student[2] == 'P':
        continue
    a+=float(student[1])*(score.get(student[2]))
    b+=float(student[1])
print(a/b)
