class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        wins=set()
        for r in range(len(nums)):
            if r-l+1>k+1:
                wins.remove(nums[l])
                l+=1
            if nums[r] in wins:
                return True
            wins.add(nums[r])
        return False
        