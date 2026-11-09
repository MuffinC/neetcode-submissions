class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for ind, v in enumerate(s):
            if v =='(': stack.append(ind)
            elif v=='*': star.append(ind)
            else:
                if stack: stack.pop()
                elif star: star.pop()
                else: 
                    return False 
        while stack and star:
             if stack.pop()>star.pop(): return False
                  
        return not stack 
        