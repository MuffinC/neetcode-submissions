class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        if amount==0: return 0
        stack=deque()

        ans=float("inf")
        seen=set()

        for x in coins:
            if amount-x==0: return 1
            else:
                if amount%x==0: ans=min(ans,amount//x) 
                seen.add(amount-x)
                stack.append( (amount-x, 1))
        while stack:
            x,y=stack.popleft()
            for z in coins:
                if x-z<0 or x-z in seen:
                    continue
                elif x-z==0: 
                    ans=min(ans,y+1)
                    return ans
                else:
                    stack.append((x-z,y+1))
                seen.add(x-z)

        return -1 if ans== float("inf") else ans