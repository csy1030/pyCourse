# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addLinkedList(self, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry:
                return ListNode(carry)
            return None
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)
        sum = l1.val + l2.val + carry
        if sum > 9:
            carry = 1
            sum %= 10
        else:
            carry = 0
        ln = ListNode(sum)
        ln.next = self.addLinkedList(l1.next, l2.next, carry)
        return ln

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        node.next = self.addLinkedList(l1, l2, 0)
        return node.next

head1 = ListNode(1)
head1.next = ListNode(8)

head2 = ListNode(0)

s = Solution()
result = []
p = s.addTwoNumbers(head1,head2)
while p:
    result.append(p.val)
    p = p.next
print(result)