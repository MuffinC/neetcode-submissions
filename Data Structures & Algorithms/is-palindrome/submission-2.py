class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        s=list(s)
        neg=0
        for x in range(0,len(s),1):
            neg-=1
            if s[x] == s[neg]: continue
            else: return False 
        return True