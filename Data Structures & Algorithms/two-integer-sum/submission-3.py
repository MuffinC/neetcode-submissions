class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(list)
        for x,y in enumerate(nums):
            d[y].append(x)
        
        for x,y in enumerate(nums):
            remainder= target -y
            if remainder in d and d[remainder][-1] != x:
                return sorted([x, d[remainder][-1]])