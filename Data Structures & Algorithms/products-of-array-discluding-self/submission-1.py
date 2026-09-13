class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[]
        for x in nums:
            if not pref:
                pref.append(x)
            else:
                pref.append(pref[-1]*x)      
        suff=[]
        cur=nums.copy()
        cur.reverse()
        for y in cur:
            if not suff:
                suff.append(y)
            else:
                suff.append(suff[-1]*y)
        suff.reverse()
        ans=[]

        for x in range(len(cur)):
            if x==0:
                ans.append(suff[x+1])
            elif x==len(cur)-1:
                ans.append(pref[x-1])
            else:
                ans.append(pref[x-1]* suff[x+1])
        return ans