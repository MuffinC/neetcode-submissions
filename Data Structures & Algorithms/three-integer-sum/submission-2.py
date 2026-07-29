class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        n=len(nums)
        seena=set()
        for a in range(0,n-2):
            if nums[a] in seena:
                continue
            seena.add(nums[a])
            l,r=a+1,n-1
            seenr=set()
            seenl=set()
            seenl.add(nums[l])
            seenr.add(nums[r])
            while l<r:
                if  nums[a] + nums[l] + nums[r] ==0: 
                     if [nums[a],nums[l],nums[r]] not in ans:
                        ans.append([nums[a],nums[l],nums[r]])
                     l+=1
                elif nums[a] + nums[l] + nums[r] >0: 
                    while r>l and nums[r] in seenr :
                        r-=1
                    seenr.add(nums[r])
                elif nums[a] + nums[l] + nums[r] <0: 
                    while l<r and nums[l] in seenl:
                        l+=1
                    seenl.add(nums[l])
        

        return ans