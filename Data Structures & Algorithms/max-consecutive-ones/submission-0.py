class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        cur=0
        for x in range(0,len(nums)):
            if nums[x] == 1:
                cur+=1
                maxi=max(maxi,cur)
            else:
                cur=0
        return maxi

        