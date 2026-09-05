class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax=nums[0]
        curmax=0
        globalmin=nums[0]
        curmin=0
        total=0

        for x in (nums):
            curmax=max(curmax+x, x)
            curmin=min(curmin+x, x)
            total+=x

            globalmax=max(globalmax,curmax)
            globalmin=min(globalmin,curmin)

        return max(globalmax, total-globalmin) if globalmax>0 else globalmax
        
        



        