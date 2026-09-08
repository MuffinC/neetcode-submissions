class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        l,r=0,0
        cur=nums[0]
        while r<len(nums) and l<len(nums):
            if cur<target:
                r+=1
                if r>=len(nums): break
                cur+=nums[r]
            else:
                ans=min(ans, r-l+1)
                cur-=nums[l]
                l+=1

                
        

        return 0 if ans==float("inf") else ans