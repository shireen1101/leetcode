# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        current = result
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10
        return result.next
        
# Test cases
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next    