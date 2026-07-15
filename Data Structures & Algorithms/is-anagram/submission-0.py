from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        curs=defaultdict(int)
        curt=defaultdict(int)

        for x in s:
            curs[x]+=1
        for x in t:
            curt[x]+=1

        for x in curs.keys():
            if x not in curt or curs[x] !=curt[x] : return False
        return True 


        