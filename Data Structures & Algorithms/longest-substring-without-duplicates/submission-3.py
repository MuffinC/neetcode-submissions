class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        cur=set()
        ans=0
        for r in range(len(s)):
            if s[r] in cur:
                while s[r] in cur:
                    cur.remove(s[l])
                    l+=1
            cur.add(s[r])
            ans=max(ans,len(cur))
        return ans
            

            
