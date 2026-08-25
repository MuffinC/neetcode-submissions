class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def backt(cur,ind):
            nonlocal ans
            if ind>len(nums) or cur in ans:
                return
            ans.append(cur.copy())
            for y in range( ind, len(nums)):
                cur.append(nums[y])
                backt(cur,y+1)
                cur.pop()
        backt([],0)
        return ans
