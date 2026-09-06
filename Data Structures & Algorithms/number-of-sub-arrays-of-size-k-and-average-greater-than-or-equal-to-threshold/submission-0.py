class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tot=0
        l=0
        ans=0
        for r in range(len(arr)):
            tot+=arr[r]
            if r-l+1==k:
                if tot/k >=threshold:
                    ans+=1
                tot-=arr[l]
                l+=1
        return ans


                

        