class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backt(cur, ind):
            nonlocal ans
            if ind>len(nums) or sum(cur)>target :
                return
            if sum(cur)==target:
                ans.append(cur.copy())
                return
            for y in range(ind,len(nums)):
                cur.append(nums[y])
                backt(cur, y)
                cur.pop()
        
        backt([],0)
        return ans