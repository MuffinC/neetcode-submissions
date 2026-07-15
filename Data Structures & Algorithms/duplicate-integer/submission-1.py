class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setu=set()
        for x in nums:
            if x not in setu: setu.add(x)
            else: return True
        return False
        