class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        total=1
        zeroc=[]
        for x in range(len(nums)):
            if nums[x] !=0: total*=nums[x]
            else: zeroc.append(x)
        ans=[]
        if len(zeroc)>1: 
            for x in range(len(nums)):
                ans.append(0)
        elif len(zeroc)==1:
            for y in range(len(nums)):
                if zeroc and y==zeroc[0]: ans.append(total)
                else: ans.append(0)
        else:
            for y in nums: ans.append(total//y)

        return ans
                    



        