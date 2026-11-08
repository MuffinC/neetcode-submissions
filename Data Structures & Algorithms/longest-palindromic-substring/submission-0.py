class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        ansl=0
        for x in range(len(s)):
            l,r=x,x

            while  l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > ansl:
                    ansl= r-l+1
                    ans=s[l:r+1]
                r+=1
                l-=1

            l,r=x,x+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > ansl:
                    ansl= r-l+1
                    ans=s[l:r+1]
                r+=1
                l-=1
        return ans


        