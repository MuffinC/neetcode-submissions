class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adjancy list
        from collections import defaultdict
       
        tab=defaultdict(list)

        for curr in prerequisites:
            tab[curr[1]].append(curr[0])
        seen=set()
        cycle=set()
        ans=[]

        def dfs(node):
            if node in seen:
                return False
            if node in cycle: 
                return True

            seen.add(node)
            for z in tab[node]:
                if not dfs(z): return False
            seen.remove(node)
            cycle.add(node)
            ans.append(node)
            return True

        
        for x in range(numCourses):
            if not dfs(x): return []
        return ans[::-1]

        