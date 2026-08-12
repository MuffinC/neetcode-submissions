class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2

        ans=[1,2]
        for x in range(0,n-2):
            ans.append(ans[-1]+ans[-2])
        return ans[-1]