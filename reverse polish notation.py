def evalRPN(tokens):
    l=0
    stack=[]
    opers={'+':lambda x,y: x+y,
           '-':lambda x,y:x-y,
           '*':lambda x,y:x*y,
           '/':lambda x,y: int(x/y)
           }
    while l<len(tokens):
        if tokens[l] not in opers:
            stack.append(int(tokens[l]))
        else:
            cur=opers[tokens[l]](stack[-2],stack[-1])
            stack=stack[:-2]
            stack.append(cur)
        l+=1
    return stack[0]
tokens=["2","1","+","3","*"]
print(evalRPN(tokens))
