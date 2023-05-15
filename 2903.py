def countP(num, point):
    point += (point-1)
    num-=1
    if num == 0:
        print(point**2)
    else:    
        countP(num, point)

num=int(input())
countP(num,2)
