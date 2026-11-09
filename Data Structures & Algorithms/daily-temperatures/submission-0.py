class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        if len(temp)==1: return [0]

        ans=[0 for x in range(len(temp))]
        import heapq
        minheap=[]
        heapq.heapify(minheap)

        for ind, v in enumerate(temp):
            if not minheap:
                heapq.heappush(minheap, (v, ind))
            else:
                while minheap:
                    if v>minheap[0][0]:
                        x,y=heapq.heappop(minheap)
                        ans[y]=ind-y
                    else: break
                heapq.heappush(minheap, (v, ind))
                
        return ans