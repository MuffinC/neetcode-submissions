class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)

        dp=[0 for x in range(len(nums)+2)]
        maxi=0

        for ind,v in enumerate(nums):
            maxi=max(dp[ind], maxi)
            dp[ind+2]=max(dp[ind]+v, maxi+v)
        return max(dp)
        

        