# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        copyHead = head
        k=1
        while copyHead:
            k+=1
            copyHead = copyHead.next
        if k%2: k = k//2+1
        else: k//=2
        
        while k:
            res = head
            head = head.next
            k -=1
        return res
        