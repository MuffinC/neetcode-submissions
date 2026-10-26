class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l=0
        seen=set()
        ans=float("-inf")
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                    
            else:
                while s[r] in seen and len(seen)!=0:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            ans=max(ans,len(seen))
        return ans