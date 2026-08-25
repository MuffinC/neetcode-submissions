class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backt(cur, ind,tot):
            nonlocal ans
            if tot==target:
                ans.append(cur.copy())
                return
            for y in range(ind, len(nums)):
                if tot +nums[y]>target:
                    break
                cur.append(nums[y])
                backt(cur, y,tot+nums[y])
                cur.pop()
        
        backt([],0,0)
        return ans