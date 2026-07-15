class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stac=[]
        for x in operations:
            if (x=="+"):
                stac.append(str(int(stac[-1])+ int(stac[-2])))
            elif (x== "C"):
                stac.pop()
            elif (x=="D"):
                stac.append(str(int(stac[-1])*2))
            else:
                stac.append(x)
        a=0
        for y in stac:
            a+=int(y)
        return a