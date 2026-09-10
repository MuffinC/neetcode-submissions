class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashs={}
        r=len(nums)-1
        while r>=0:
            if nums[r] not in hashs:
                hashs[nums[r]]=1
            else:
                hashs[nums[r]]+=1
                if hashs[nums[r]] >2:
                    hashs[nums[r]]-=1
                    nums.pop(r)

            r-=1
        return sum(hashs.values())



        