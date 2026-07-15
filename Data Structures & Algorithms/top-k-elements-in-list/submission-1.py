class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hold={}
        for x in nums:
            if x not in hold: hold[x]=1
            else: hold[x] +=1
        print(hold)
        t=[]
        for ke,v in hold.items():
            t.append((ke,v))
        cur=sorted(t, reverse=True, key=lambda x:x[1])
        ans=[]
        for x in range(0,k):
            ans.append(cur[x][0])
        
        return ans
        