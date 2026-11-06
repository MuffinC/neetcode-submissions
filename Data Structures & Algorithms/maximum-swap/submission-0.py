class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<10: return num
        ans=num
        num=list(str(num))
        tab={}
        for ind,v in enumerate(num):
            if int(v) not in tab:
                tab[int(v)]=[ind]
            else:
                tab[int(v)].append(ind)

        l=0
        while l< len(num):
            if int(num[l])==9:
                tab[9].pop(0)
            else:
                for x in range(9, int(num[l]),-1):
                    if x in tab and tab[x]:
                        ind=tab[x].pop()
                        hold=num[ind]
                        num[ind]=num[l]
                        num[l]=hold
                        ans=max(ans, int("".join(num)))
                        return ans
                tab[int(num[l])].pop(0)
            l+=1

        return ans