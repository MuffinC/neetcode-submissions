class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start=set()
        for x in nums:
            if x in start: return x
            start.add(x)
            
        