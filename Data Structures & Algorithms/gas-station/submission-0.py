class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans=0
        n=len(gas)
        l=0
   
        while l<n:
            if gas[l]>=cost[l]:
                cur=gas[l]
                for r in range(l,l+n+1,1):  
                    cur=cur-cost[r%n] 
                    if cur<0: break
                    cur+=gas[(r+1)%n]
                if cur>=0: return l
                l=r
            else:l+=1

        return -1

