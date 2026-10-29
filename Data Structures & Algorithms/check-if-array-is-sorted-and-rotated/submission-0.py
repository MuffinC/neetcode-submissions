class Solution:
    def check(self, nums: List[int]) -> bool:
        drop=0
        n=len(nums)
        for x in range(n):
            if nums[x]> nums[(x+1)%n]:
              drop+=1  
            if drop>1: return False
        return True