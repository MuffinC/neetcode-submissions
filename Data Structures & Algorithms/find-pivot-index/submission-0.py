class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        mat=[]

        for x in range(len(nums)-1,-1,-1):
            if not mat: mat.append(nums[x])
            else:
                mat.append(mat[-1]+nums[x])

        mat.reverse()
        cur=0
        for y in range(len(nums)):
            if cur==mat[y]-nums[y]:
                return y
            cur+=nums[y]
        return -1


        