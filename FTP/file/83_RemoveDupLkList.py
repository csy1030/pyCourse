# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ori_head = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        result = []
        while ori_head.next:
            result.append(ori_head.val)
            ori_head = ori_head.next
        return result

s = Solution()
print(s.deleteDuplicates())
