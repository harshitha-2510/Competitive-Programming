

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={')':'(','}':'{',']':'['}
        for i in s:
            if i in map.values():
                stack.append(i)
            elif stack and map[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]


        
