class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for c in range(len(s)):
            if c==0:continue
            ans+=abs(ord(s[c-1])-ord(s[c]))
        return ans