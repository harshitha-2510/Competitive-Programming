#fibonacci using dynamic programming
def fibonacci(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2)
    return f[n]
print(fibonacci(5))




#fibonacci using recursion
def fibonacci(n):
    print(n)
    if n<= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



#function for nth fibonacci number
def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
print(fibonacci(9))
