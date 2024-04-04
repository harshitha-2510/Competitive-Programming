#tribonacci series

def tribonacci(n):
    if n<=1:
        return n
    elif n==2:
        return 1
    first,second,third=0,1,1
    for _ in range(3,n+1):
        first,second,third=second,third,first+second+third
    return third
num=int(input("enter which tribonacci number you want to know?"))
print(tribonacci(num))
    
