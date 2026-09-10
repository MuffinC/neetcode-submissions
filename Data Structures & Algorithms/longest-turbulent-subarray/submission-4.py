class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<2: return 1
        pasts=""
        curs=""
        ans=1
        curtot=1
        for r in range(1,len(arr)):
            if arr[r-1]>arr[r]:
                curs=">"
            elif arr[r-1]<arr[r]:
                curs="<"
            else:
                curs=""
                curtot=1
                continue

            if (pasts==">" and curs=="<") or (pasts=="<" and curs==">") or (pasts=="" and curs=="<") or (pasts=="" and curs==">"):
                curtot+=1
                ans=max(ans, curtot)
            else:
                curtot=2
            pasts=curs

        return ans
        