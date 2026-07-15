class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hold={}
        ans=[]
        for x in strs:
            if "".join(sorted(x)) not in hold: hold["".join(sorted(x))]=[x]
            else: hold["".join(sorted(x))].append(x)
        for k in hold.keys():
            ans.append(hold[k])


        return ans