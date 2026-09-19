# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        start=head
        arr=[]
        while start:
            arr.append(start.val)
            start=start.next
        ans=0
        for x in range(len(arr)//2):
            cur=arr[x] +arr[len(arr)-x-1]
            ans=max(ans, cur)
        return ans