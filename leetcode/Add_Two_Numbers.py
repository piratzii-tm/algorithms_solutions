# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        L1 = []
        while l1:
            L1.append(l1.val)
            l1 = l1.next
        L2 = []
        while l2:
            L2.append(l2.val)
            l2 = l2.next
        while len(L1)>len(L2):L2.append(0)
        while len(L1)<len(L2):L1.append(0)
        
        s = []
        t = 0

        for i in range(len(L1)):
            s.append((L1[i]+L2[i]+t)%10)
            t = (L1[i]+L2[i]+t) // 10
        if t!=0: s.append(t)

        a = ListNode(0)
        temp = a
        for i in s:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next