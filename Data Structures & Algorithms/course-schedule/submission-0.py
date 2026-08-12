class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        #loop detection
        table={x:[]for x in range(numCourses)}
        for x,y in pre:
            table[y].append(x)
        seen=set()
        
        def dfs(z):
            if z in seen: 
                return False
            if not table[z]: return True
            seen.add(z) 
            for i in table[z]:
                if not dfs(i): return False
            seen.remove(z)
            table[z]=[]
            return True

        for x in range(numCourses):
            if not dfs(x): return False
        return True
        