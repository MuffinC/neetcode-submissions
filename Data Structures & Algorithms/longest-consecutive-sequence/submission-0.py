class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        stack=[]
        ans=1
        nums=list(sorted(nums))
        for x in nums:
            if not stack: 
                stack.append(x)
                continue
            if x==stack[-1]+1:
                stack.append(x)
                ans=max(ans,len(stack))
            elif x==stack[-1]: continue
            else: 
                stack=[x]
        return ans
        