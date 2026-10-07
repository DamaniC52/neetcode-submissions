# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None        # nothing is behind the first node yet
        curr = head        # start at the first node

        while curr:                 # keep going until we fall off the end
            nxt = curr.next         # 1. save the rest of the list
            curr.next = prev        # 2. flip the arrow backward
            prev = curr             # 3. step prev forward
            curr = nxt              # 4. step curr forward

        return prev                 # prev is on the old last node = new head