class Solution:
    def isValid(self, s: str) -> bool:
        stac=[]
        for x in s:
            if x=='[' or x=='(' or x=='{':
                stac.append(x)
            elif stac and stac[-1]=='[' and x==']': stac.pop()
            elif stac and stac[-1]=='(' and x==')': stac.pop()
            elif stac and stac[-1]=='{' and x=='}': stac.pop()
            else: return False
        
        if len(stac)>0: return False
        return True

        