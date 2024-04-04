def climbstairs(n):
    if n==0 or n==1 or n==2:
        return n
    else:
        res, step_1, step_2 =0, 1, 2
        for i in range(2, n):
            res= step_2+step_1
            step_1=step_2
            step_2=res
        return res
    
