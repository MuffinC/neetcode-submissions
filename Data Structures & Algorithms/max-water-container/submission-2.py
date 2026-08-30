class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=float("-inf")
        l,r=0,len(heights)-1
        while l<r:
            area=(r-l)*min(heights[r],heights[l])
            ans=max(ans,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return ans