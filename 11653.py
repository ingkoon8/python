num=int(input())

def divide(num):
    if num == 2:
        print(num)
        return 0
    for i in range(2, num+1):
        if num % i == 0:
            print(i)
            if i == num+1:
                break
            else:
                divide(num//i)
                break
    return 0

divide(num)
